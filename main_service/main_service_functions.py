import random
import json
import pulp
import time



def get_results(body):
    if body is None:
        body = {}
    no_suppliers = body.get("no_suppliers", 3)
    no_parts = body.get("no_parts", 4)
    return generate_data(no_suppliers=no_suppliers, no_parts=no_parts)


def post_results(body):
    time.sleep(100)
    return solve(body)


def delete_results():
    return {"results": "example_delete"}


def generate_data(no_suppliers, no_parts):
    suppliers = {}
    parts = {}

    # generate suppliers and their bids
    for supplier_no in range(no_suppliers):
        key_supplier = "Supplier " + str(supplier_no + 1)
        suppliers[key_supplier] = {
            "Parts": {},
            "min_revenue": random.randint(50, 100),
            "max_parts": random.randint(20, 500),
        }
        for part_no in range(no_parts):
            key_part = "Part " + str(part_no + 1)
            suppliers[key_supplier]["Parts"][key_part] = random.randint(20, 1000)

    # generate part no with the preferred suppliers
    for part_no in range(no_parts):
        key_part = "Part " + str(part_no + 1)
        parts[key_part] = {
            "preferred_supplier": random.sample(list(suppliers.keys()), k=random.randint(2, min(no_suppliers, 200))),
            "count_orders": random.randint(20, 100),
        }
    return {"parts": parts, "suppliers": suppliers}


def solve(data):
    parts, suppliers = data["parts"], data["suppliers"]
    model = pulp.LpProblem("Resource Allocation Problem", pulp.LpMinimize)
    # define a dictionary that matches teh number of parts a certain supplier provides
    part_supplier_count = {}
    for part_no, part_details in parts.items():
        for supplier_no in suppliers.keys():
            if supplier_no in part_details["preferred_supplier"]:
                part_supplier_count[(part_no, supplier_no)] = pulp.LpVariable(
                    f"{supplier_no};_{part_no}",
                    lowBound=0,
                    upBound=part_details["count_orders"],
                    cat="Integer",
                )

    # constraint 1: match for many parts are needed
    for part_no, part_details in parts.items():
        part_count = 0
        for supplier_no in suppliers.keys():
            if supplier_no in part_details["preferred_supplier"]:
                part_count += part_supplier_count[(part_no, supplier_no)]
        model += part_count == part_details["count_orders"]

    # constraint 2: each supplier has a minimum revenue coming out of this bid round
    # constraint 3: maximimum capacity for each supplier
    for supplier_no, supplier_details in suppliers.items():
        model += (
            pulp.lpSum(
                part_supplier_count[(part_no, supplier_no)] * supplier_details["Parts"][part_no]
                for part_no, part_details in parts.items()
                if supplier_no in part_details["preferred_supplier"]
            )
            >= supplier_details["min_revenue"]
        )
        model += (
            pulp.lpSum(
                1 for part_no, part_details in parts.items() if supplier_no in part_details["preferred_supplier"]
            )
            <= supplier_details["max_parts"]
        )

    # objective function: minimise cost
    cost = 0
    for part_no, part_details in parts.items():
        for supplier_no, supplier_details in suppliers.items():
            if supplier_no in part_details["preferred_supplier"]:
                cost += part_supplier_count[(part_no, supplier_no)] * supplier_details["Parts"][part_no]
    model += cost
    model.solve()

    out_data = []

    for v in model.variables():
        if v.varValue:
            supplier, part = [x.replace("_", " ") for x in v.name.split(';_')]
            out_data.append({"supplier": supplier, "part": part, "quantity": v.varValue})

    return out_data
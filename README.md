Instructions for making a new microservice ** SOFTWARE TEAM **

The following details creation of a new microservice using our framework repo. 

1. Create a new repo via github.com. e.g. "backend-example1"
2. Begin in our framework repo "backend-framework"
3. Add a new remote repo to backend-framework
```
git remote add example1 git@github.com:r2dl/backend-example1.git
```
4. Push the backend-framework main to the example1 remote main
```
git push example1 main:main
```

This results in a new repo linked to backend-framework CI/CD pipeline, ready for development.
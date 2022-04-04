###Instructions for making a new microservice
_(FOR USE BY SOFTWARE TEAM)_

The following details creation of a new microservice using our framework repo. 

1. Create a new repo via gitHub.com e.g. "backend-example1"
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

___

##Instuctions for developing a microservice:
- Start from the main branch ```git checkout main```
- To add a new feature make a new branch from main ```git branch [FEATURE_BRANCH_NAME]```
- Move to the feature branch ```git checkout [FEATURE_BRANCH_NAME]```
- To install a library use the command ```poetry add [LIBRARY_NAME_AND_VERSION]```
- To update your branch with changes from main enter the following commands:
```
git fetch
git merge origin/main
fix merge conflicts on the README.md file
git add README.md
git push
```
- Write your methods in the ```main_service.py``` and return your results in the following format: 
```
{"results": []}
```
- Add and commit your changes (for guidance see the Add & Commit Changes section of [this tutorial](https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/))
- Push to the feature branch ```git push origin [FEATURE_BRANCH_NAME]```
- Create a pull request to [YOUR_BRANCH_NAME] (for guidance see [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request))
- Ask one or two developers/product owner for review


###Updates to framework
- When the framework is updated this will automatically trigger updates in your repo
- The ```base``` branch of your repo will be updated
- A pull request will be opened from ```base``` into ```main```
- Unless you have made changes to the framework code, any merge conflicts should be minimal and we can advise on resolution


# Syntax: BRANCH='<Branch Name>' make delete_branch
delete_branch:
	git checkout master
	git branch -d $(BRANCH)


# Syntax: BRANCH='<Branch Name>' make create_new_branch
create_new_branch:
	git pull origin master
	git checkout -b $(BRANCH)

# Only to use in created Branch
# Syntax: BRANCH='<Branch Name>' make update_current_branch
update_current_branch:
	git add .
	git commit -m 'Update from master'

	git checkout master
	git pull origin master

	git checkout $(BRANCH)
	git merge master

# Syntax: make update_requirements
make update_requirements:
	@pip freeze > requirements.txt

# Syntax: make start_local_server
# URL: http://localhost:8000/
# To shut down the server simply press Strg + C (Mac: Ctrl + C) in the corresponding terminal
make start_local_server:
	uvicorn api.api:app --reload

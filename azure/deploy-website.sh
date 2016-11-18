echo "Deploying website content ${deployed.name} on ${deployed.container.name} Microsoft Azure Website"
git clone git@github.com:${deployed.githubRepository}.git workingdir
cp -r ${deployed.file}/* ./workingdir
cd workingdir
git add -A
git commit -a -m "Commit for Deployment of ${deployed.deployedApplication.version.application.name}/${deployed.deployedApplication.version.name}"
git push



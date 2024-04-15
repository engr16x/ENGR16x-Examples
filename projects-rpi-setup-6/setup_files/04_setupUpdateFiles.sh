echo
echo "Setting up file structure to sync with github update repositories"

mkdir /home/pi/Desktop/updates
cd /home/pi/Desktop/updates

echo
echo "Setting up projects-updates/boat"
sudo rm -r boat
mkdir boat
cd boat
git init
git config core.sparsecheckout true
echo boat/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/design-challenge"
sudo rm -r design-challenge
mkdir design-challenge
cd design-challenge
git init
git config core.sparsecheckout true
echo design-challenge/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/donut"
sudo rm -r donut
mkdir donut
cd donut
git init
git config core.sparsecheckout true
echo donut/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/duck"
sudo rm -r duck
mkdir duck
cd duck
git init
git config core.sparsecheckout true
echo duck/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/elephant"
sudo rm -r elephant
mkdir elephant
cd elephant
git init
git config core.sparsecheckout true
echo elephant/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/in-class-activities"
sudo rm -r in-class-activities
mkdir in-class-activities
cd in-class-activities
git init
git config core.sparsecheckout true
echo in-class-activities/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/plane"
sudo rm -r plane
mkdir plane
cd plane
git init
git config core.sparsecheckout true
echo plane/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..

echo
echo "Setting up projects-updates/projects"
sudo rm -r projects
mkdir projects
cd projects
git init
git config core.sparsecheckout true
echo projects/ >> .git/info/sparse-checkout
git remote add -f origin https://github.com/engr16x/projects-updates.git
git pull origin master
cd ..
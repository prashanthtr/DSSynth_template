
#!/bin/bash

# can give all the files as commandline parameters 

list=`find $1 -name '.*git'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '.*git'`)

if [ ${#list[@]}  -eq 0 ];
then
echo "removed .git files"
else
echo "${#list[@]} Git Files still remaining"
fi
	
list=`find $1 -name '.*DS_Store'`

for f in $list
do 
	sudo rm "$f" 
done

list=(`find $1 -name '.*DS_Store'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed .DS_Store"
else
echo "${#list[@]} .DSStore Files still remaining"
fi

list=`find $1 -name '.__pycache__'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '.__pycache__'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed pycache files"
else
echo "${#list[@]} pycache Files still remaining"
fi


list=`find $1 -name '.gitignore'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '.gitignore'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed gitignore files"
else
echo "${#list[@]} pycache Files still remaining"
fi

list=`find $1 -name '.ipynb_checkpoints'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '.ipynb_checkpoints'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed notebook ipynb files"
else
echo "${#list[@]} checkpoint Files still remaining"
fi


list=`find $1 -name '.*DSMac'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '.*DSMac'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed .DSMac files"
else
echo "${#list[@]} DSMAC Files still remaining"
fi


list=`find $1 -name '*.egg-info'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find $1 -name '*.egg-info'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed egg-info files from git repos"
else
echo "${#list[@]} egg-info Files still remaining"
fi

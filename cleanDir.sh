
#!/bin/bash

# can give all the files as commandline parameters 

list=`find ./Synth -name '.*git'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find ./Synth -name '.*git'`)

if [ ${#list[@]}  -eq 0 ];
then
echo "removed .git files"
else
echo "${#list[@]} Git Files still remaining"
fi
	
list=`find ./Synth -name '.*DS_Store'`

for f in $list
do 
	sudo rm "$f" 
done

list=(`find ./Synth -name '.*DS_Store'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed .DS_Store"
else
echo "${#list[@]} .DSStore Files still remaining"
fi

list=`find ./Synth -name '.*__pycache__'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find ./Synth -name '.*__pycache__'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed pycache files"
else
echo "${#list[@]} pycache Files still remaining"
fi


list=`find ./Synth -name '.*.git_ignore'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find ./Synth -name '.*.git_ignore'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed gitignore files"
else
echo "${#list[@]} pycache Files still remaining"
fi


list=`find ./Synth -name '.*ipynb_checkpoints'`

for f in $list ; do 
  sudo rm -r "$f"
done

list=(`find ./Synth -name '.*ipynb_checkpoints'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed notebook ipynb files"
else
echo "${#list[@]} checkpoint Files still remaining"
fi


list=(`find ./Synth -name '.*.DSMac'`)

if [ ${#list[@]} -eq 0 ];
then
echo "removed .DSMac ipynb files"
else
echo "${#list[@]} DSMAC Files still remaining"
fi
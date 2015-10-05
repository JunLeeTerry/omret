#!/bin/sh

message=`date +%Y%m%d`
cd ~/git_JunLeeTerry/omret;
cp -r ~/omret_9_17/omret ~/git_JunLeeTerry/omret/;
git add .;

echo "Enter the commit message: \c"
read INPUT
if ( $INPUT == "" ) ; then
    git commit -m $message;
else 
    git commit -m $INPUT;
fi

#git commit -m $message;
git push;
#!/bin/bash

function set(){

if [[ -e "enc" ]];then
    sudo chmod +x enc
    sudo mv enc /bin
    echo -e  "Done \n type enc -h"
else
    echo -e "  =========== failed ========= " 
fi

}


if ping -c 2 -W 5 8.8.8.8 > /dev/null 2>&1; then
        echo "Internet is connected."
	wget https://github.com/OneKnow654/Enc/releases/download/Oneknown654/enc 
	set()
    else
        echo "No internet connection."
    fi



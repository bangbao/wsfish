#/bin/bash

ENV_NAME=local
PYTHON_BIN="/usr/local/bin/python"
if ! [ -x "$PYTHON_BIN" ]; then
    PYTHON_BIN="/usr/bin/python";
fi

OSNAME=(`uname -s`)
P_DIR=$(cd `dirname $0`; pwd -P)
export PYTHONPATH=${PYTHONPATH}${P_DIR}
export PYTHONIOENCODING=UTF-8

if [ `uname -n` == "iZ25ysyv8v6Z" ]; then
    PRODUCT_DIR=/data/sites/yp/server_${ENV_NAME}
else
    PRODUCT_DIR=$P_DIR
fi


shell()
{
    ipython -i $P_DIR/scripts/myshell.py $ENV_NAME $1 $2 $3 $4
}

start()
{
    #git merge develop && $PYTHON_BIN -O ${P_DIR}/run.py --port=58400 --debug=true --log_file_prefix=${P_DIR}/logs/nba-58400.log & echo 'restart success'
    $SUPERVISORCTL start $PROGRAM_NAME:*
}

stop()
{
    $SUPERVISORCTL stop $PROGRAM_NAME:*
}

restart()
{
    for i in `$SUPERVISORCTL status | grep $PROGRAM_NAME | awk '{print $1}'`;
    do
        $SUPERVISORCTL restart $i;
    done
}

runscript()
{
    #LOAD_SOURCE=true
    SCRIPT_NAME="${P_DIR}/scripts/$1.py"

    if [ -r ${SCRIPT_NAME} ]; then
        $PYTHON_BIN $SCRIPT_NAME $ENV_NAME $2 $3
        echo
        echo 'runscript done.'
    fi
}

set_envname()
{
    envname=$1
    echo "OSNAME=${OSNAME}"
    if [ "$OSNAME" == "Darwin" ]; then
        sed -i '' "3s/^ENV_NAME=.*$/ENV_NAME=${envname}/g" ${P_DIR}/control.sh;
        sed -i '' "s/^ENV_NAME = \".*\"$/ENV_NAME = \"${envname}\"/g" ${P_DIR}/manage.py;
        sed -i '' "s/^ENV_NAME = \".*\"$/ENV_NAME = \"${envname}\"/g" ${P_DIR}/wsgi.py;
    else
        sed -i "3s/^ENV_NAME=.*$/ENV_NAME=${envname}/g" ${P_DIR}/control.sh;
        sed -i "s/^ENV_NAME = \".*\"$/ENV_NAME = \"${envname}\"/g" ${P_DIR}/manage.py;
        sed -i "s/^ENV_NAME = \".*\"$/ENV_NAME = \"${envname}\"/g" ${P_DIR}/wsgi.py;
    fi
}

case "$1" in
    start) start;;
    stop) stop;;
    restart) restart;;
    set_envname) set_envname $2 $3 $4;;
    shell) shell $2 $3 $4;;
    *) shell $1 $2 $3 $4;;
esac


SCRIPTS_PATH=$(dirname $(readlink -f $0))
PROJECT_PATH=$(dirname $SCRIPTS_PATH)
FLOG_PATH=$PROJECT_PATH/flog

dramatiq flog.actors --watch $FLOG_PATH $@

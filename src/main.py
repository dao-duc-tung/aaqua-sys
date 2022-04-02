import logging
import os

from apis import ServiceCtrl, flask_app, serve_InvocationService
from data_module import RedisDatabaseMgr
from model_module import ModelFramework, ModelMgr, PathModelSource
from utils import AppConst, DefaultApiValues, setup_logger

setup_logger()
logger = logging.getLogger(AppConst.APP_NAME)
logger.info(f"NEW SESSION")


def run_service(grpc_port, rest_port):
    serve_InvocationService(grpc_port, wait=False)
    # Must use 0.0.0.0 for docker
    flask_app.run(host="0.0.0.0", port=rest_port)


if __name__ == "__main__":
    # Define resources
    # MODEL_PATH = "file://../models/tf_face_det"
    MODEL_PATH = (
        "https://tungdao-public.s3.ap-southeast-1.amazonaws.com/tf_face_det.zip"
    )
    MODEL_FRAMEWORK = ModelFramework.TENSORFLOW

    model_mgr = ModelMgr(MODEL_FRAMEWORK)
    db_mgt = RedisDatabaseMgr()
    path_model_src = PathModelSource(MODEL_PATH)

    # Init ServiceCtrl
    if not ServiceCtrl.initialize(model_mgr, db_mgt):
        exit(1)
    ServiceCtrl.set_model_source(path_model_src)

    GRPC_PORT = os.getenv("GRPC_PORT", DefaultApiValues.GRPC_PORT)
    REST_PORT = os.getenv("REST_PORT", DefaultApiValues.REST_PORT)
    run_service(GRPC_PORT, REST_PORT)

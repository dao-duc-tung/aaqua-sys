from model_module.model_io import ModelInput, ModelOutput


class IDatabaseMgt:
    @property
    def is_connected(self) -> bool:
        raise NotImplementedError()

    def connect(self, *args, **kwargs):
        raise NotImplementedError()

    def close(self, *args, **kwargs):
        raise NotImplementedError()

    def save_model_input(self, model_input: ModelInput, *args, **kwargs):
        raise NotImplementedError()

    def save_model_output(
        self, model_input: ModelInput, model_output: ModelOutput, *args, **kwargs
    ):
        raise NotImplementedError()

    def retrieve_model_input(self, model_input_id: str, *args, **kwargs):
        raise NotImplementedError()

    def retrieve_model_output(self, model_input_id: str, *args, **kwargs):
        raise NotImplementedError()


class InMemoryDatabaseMgt(IDatabaseMgt):
    @property
    def is_connected(self) -> bool:
        return True

    def __init__(self) -> None:
        self._model_input_dict = {}
        self._model_output_dict = {}

    def connect(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs):
        pass

    def save_model_input(self, model_input: ModelInput, *args, **kwargs):
        self._model_input_dict[model_input.id] = model_input

    def save_model_output(
        self, model_input: ModelInput, model_output: ModelOutput, *args, **kwargs
    ):
        self._model_output_dict[model_input.id] = model_output

    def retrieve_model_input(self, model_input_id: str, *args, **kwargs):
        if model_input_id in self._model_input_dict:
            return self._model_input_dict[model_input_id]
        return None

    def retrieve_model_output(self, model_input_id: str, *args, **kwargs):
        if model_input_id in self._model_output_dict:
            return self._model_output_dict[model_input_id]

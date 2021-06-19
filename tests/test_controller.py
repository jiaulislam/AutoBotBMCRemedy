from excel.controller import CRController
from utilites.static_data import StaticData


def test_file_open():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    assert _controller.get_column_count() == 50


def test_data_validation_1():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(2)
    assert data.get(2) == "CRQ000000335378"


def test_data_validation_2():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(3)
    assert data.get(3) is not None


def test_data_validation_3():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(2)
    assert data.get(3) is None


def test_file_name():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    assert repr(_controller) == "CR_STATUS.xlsx"


def test_status_cell():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(2)
    assert data.get(7) == "CLOSED"


def test_status_cell_1():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(50)
    assert data.get(7) == "CLOSED"


def test_last_row_data():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    data = _controller.get_row(12)
    assert data.get(2) == "CRQ000000335358"


def test_insert_1():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    _controller.insert("CANCELLED", 2)
    _controller.save()
    _controller.close()
    assert True


def test_insert_2():
    _controller = CRController(StaticData.CONTROLLER_FILE)
    _col_count = _controller.get_column_count()
    for i in range(2, _col_count + 2):
        _controller.insert("CLOSED", i)
    _controller.save()
    _controller.close()
    assert True

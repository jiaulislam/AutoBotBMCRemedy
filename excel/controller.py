from typing import Dict
from excel.excel import Excel


class CRController(Excel):

    def __init__(self, file: str) -> None:
        super().__init__(file)

    def get_row(self, row_num: int) -> Dict[int, str]:
        _row_data = {}
        _row_num = row_num + 1
        for _idx, _cell_chr in enumerate(range(65, 72), start=1):
            _cell_idx = f'{chr(_cell_chr)}{_row_num}'
            _row_data[_idx] = self._ws[_cell_idx].value
        
        return _row_data

    def insert(self, status: str, index: int) -> None:
        _cell_index = f'G{index}'
        self._ws[_cell_index] = status

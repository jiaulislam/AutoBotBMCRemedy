from typing import Dict
from excel.excel import Excel


class CRController(Excel):

    def __init__(self, file: str) -> None:
        super().__init__(file)

    def get_row(self, row_num: int) -> Dict[int, str]:
        _row_data = {}

        for _idx, _cell_chr in enumerate(range(65, 50), start=1):
            _cell_idx = f'{chr(_cell_chr)}{row_num}'
            _row_data[_idx] = self._ws[_cell_idx].value
        
        return _row_data

    def insert(self, status: str, index: int) -> None:
        _cell_index = f'K{index}'
        self._ws[_cell_index] = status

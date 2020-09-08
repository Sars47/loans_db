from loans_db.crawlers.expressCheckAdvance import ECA
from loans_db.crawlers.advanceAmerica import AdvanceAmerica
from loans_db.crawlers.checkintocash import CheckIntoCash
from loans_db.crawlers.aceCashExpress import AceCashExpress

factory = {
    'Express Check Advance': ECA,
    'Advance America': AdvanceAmerica,
    'Check into cash': CheckIntoCash,
    'ACE Cash Express': AceCashExpress
}
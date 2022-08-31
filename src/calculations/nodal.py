from shapely.geometry import Polygon as SPolygon, Point, LineString

from models.models import NodalCalcDecision


def calc_nodal(vlp: dict, ipr: dict):
    """
    Расчёт точки пересечения VLP vs IPR

    Parameters
    ----------
    vlp : dict
        Словарь, содержащий VLP
    ipr : dict
        Словарь, содержащий IPR
    """

    # Populate R-tree index with bounds of grid cells
    well = LineString(zip(vlp["q_liq"], vlp["p_wf"]))
    plast = LineString(zip(ipr["q_liq"], ipr["p_wf"]))
    point = well.intersection(plast)
    print(point)
    parse_point = NodalCalcDecision(p_wf = point.y, q_liq=point.x).dict()
    return [parse_point]
    # Можно использовать numpy или библиотеку Shapely, LineString intersection
    pass


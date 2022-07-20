from astroquery.simbad import Simbad

__all__ = ['AQueryTest']


class AQueryTest:
    def __init__(self):
        pass

    def run(self):
        Simbad.add_votable_fields('flux(U)', 'flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'flux(J)', 'sptype',
                                  'parallax', 'pm', 'z_value')
        table = Simbad.query_object('3C273')

        if table is None:
            raise RuntimeError("Could not query.")

        return table

    def run_fail(self):
        Simbad.add_votable_fields('flux(U)', 'flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'flux(J)', 'sptype',
                                  'parallax', 'pm', 'z_value')
        table = Simbad.query_object('BLAH')

        if table is None:
            raise RuntimeError("Could not query.")

        return table

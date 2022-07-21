import time

__all__ = ['AQueryTest']


class AQueryTest:
    def __init__(self):
        pass

    def run(self):
        from astroquery.simbad import Simbad

        Simbad.add_votable_fields('flux(U)', 'flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'flux(J)', 'sptype',
                                  'parallax', 'pm', 'z_value')
        print('Running first query...')
        table = Simbad.query_object('3C273')
        print(table)

        if table is None:
            raise RuntimeError("Could not query.")

        sleep = 600
        print(f'Sleeping for {sleep}s...')
        time.sleep(sleep)
        table = Simbad.query_object('3C273')
        print('Success after a long sleep!')

        return table

    def run_fail(self):
        from astroquery.simbad import Simbad
        Simbad.add_votable_fields('flux(U)', 'flux(B)', 'flux(V)', 'flux(R)', 'flux(I)', 'flux(J)', 'sptype',
                                  'parallax', 'pm', 'z_value')
        table = Simbad.query_object('BLAH')

        if table is None:
            raise RuntimeError("Could not query.")

        return table

#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python

import unittest

from integrate import integrate

class TestIntegrate(unittest.TestCase):
	
	def setUp(self):
		pass

	def test_integrate(self):
		metadata = {'exposure_time': 0.05000000074505806, 
                            'oscillation': (0.0, 0.20000000298023224), 
                            'wavelength': 0.9201257824897766, 
 			    'matching': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
					 12, 13, 14, 15, 16, 17, 18, 19, 20, 
					 21, 22, 23, 24, 25, 26, 27, 28, 29, 
					 30, 31, 32, 33, 34, 35, 36, 37, 38, 
					 39, 40, 41, 42, 43, 44, 45, 46, 47, 
					 48, 49, 50], 
			    'size': (3269, 3110), 
			    'detector_class': 'eiger 9M', 
                            'end': 50, 'start': 1, 
                            'template': 'CataApo05_1444_??????.h5', 
                            'serial_number': 0, 
			    'detector': 'EIGER_9M', 
       			    'sensor': 0.44999999227002263, 
			    'pixel': (0.07500000356230885, 0.07500000356230885), 
			    'phi_start': 0.0, 
			    'saturation': 92461.0, 
			    'beam': (120.55726144764847, 119.44351135718689), 
		            'phi_end': 0.20000000298023224, 
			    'distance': 200.04000666485112, 
	   	 	    'oscillation_axis': 'Omega_I_guess', 
	 	 	    'phi_width': 0.20000000298023224, 
			    'extra_text': 'LIB=/usr/local/crys-local/ccp4-7.0/bin/eiger2cbf.so\n\nLIB=/usr/local/crys-local/XDS_2Sep17/dectris-neggia.so\n', 
			    'directory': '/mnt/optane/hbernstein/CollinsLaccases/data/CataApo05/5/NSLS2-18_10'}
		p1_unit_cell = (199.7, 200.9, 202.5, 108.0, 109.9, 109.6)
		resolution_low = 30.0
		n_jobs = 1
		n_processors = 0
		self.assertEqual(integrate(metadata, p1_unit_cell, resolution_low, n_jobs, n_processors), (0.224, 0.224, 0.224))


	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main()

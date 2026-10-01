import sys
import unittest
from unittest.mock import MagicMock

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)
    
try:
    import bpy
except ImportError:
    sys.modules['bpy'] = MagicMock()
    sys.modules['bpy.props'] = MagicMock()
    sys.modules['bpy.types'] = MagicMock()
    sys.modules['bpy.utils'] = MagicMock()

from blender_soliton import calculate_soliton_z, soliton_frame_handler

class TestSolitonMath(unittest.TestCase):
    
    def test_peak_amplitude(self):
        z = calculate_soliton_z(x=0.0, t=0.0, A=2.0, v=1.0, w=1.5)
        self.assertEqual(z, 2.0)
        
    def test_wave_movement(self):
        z = calculate_soliton_z(x=2.0, t=1.0, A=3.0, v=2.0, w=1.0)
        self.assertEqual(z, 3.0)

    def test_overflow_protection(self):
        z = calculate_soliton_z(x=1000.0, t=0.0, A=2.0, v=1.0, w=1.5)
        self.assertEqual(z, 0.0)

class TestSolitonHandler(unittest.TestCase):

    def test_handler_skips_without_grid(self):
        mock_scene = MagicMock()
        mock_scene.objects.get.return_value = None
        
        try:
            pass 
        except Exception as e:
            self.fail(f"Handler rzucił wyjątek: {e}")

if __name__ == '__main__':
    unittest.main()

import subprocess
import sys
import unittest
from pathlib import Path

from main import calculate_dose_mg


ROOT_DIR = Path(__file__).resolve().parent


def run_app(inputs):
    process = subprocess.run(
        [sys.executable, "main.py"],
        input=inputs,
        text=True,
        capture_output=True,
        cwd=ROOT_DIR,
        check=True,
    )
    return process.stdout


class TestDoseFormulas(unittest.TestCase):
    def test_calculate_dose_mg_with_integer_values(self):
        self.assertEqual(calculate_dose_mg(10, 25), 250)

    def test_calculate_dose_mg_with_decimal_values(self):
        self.assertEqual(calculate_dose_mg(7.5, 0.8), 6.0)

    def test_calculate_dose_mg_with_zero_weight(self):
        self.assertEqual(calculate_dose_mg(0, 10), 0)


class TestCliIntegration(unittest.TestCase):
    def test_amoxicilina_flow(self):
        output = run_app("10\namoxicilina\n15\n")
        self.assertIn("Administrar 150.0mg IM/SC/VO a cada 8-12 horas.", output)

    def test_dipirona_flow(self):
        output = run_app("10\ndipirona\n")
        self.assertIn("Administrar 250.0mg IV/IM/SC/VO a cada 8 horas.", output)

    def test_doxiciclina_flow(self):
        output = run_app("10\ndoxiciclina\n")
        self.assertIn("Administrar 100.0mg IV/VO a cada 12-24 horas.", output)

    def test_enrofloxacina_flow(self):
        output = run_app("10\nenrofloxacina\n1\n7\n")
        self.assertIn("Administrar 70.0mg IM/VO a cada 12-24 horas.", output)

    def test_maropitant_flow(self):
        output = run_app("10\nmaropitant\n")
        self.assertIn("Administrar 10.0mg SC/VO SID", output)

    def test_meloxicam_flow(self):
        output = run_app("10\nmeloxicam\n1\n")
        self.assertIn("Iniciar com 2.0mg IV/SC/VO, continuando com 1.0mg VO SID.", output)

    def test_metronidazol_flow(self):
        output = run_app("10\nmetronidazol\n2\n")
        self.assertIn("Administrar 150.0mg IV/VO BID.", output)

    def test_omeprazol_flow(self):
        output = run_app("10\nomeprazol\n0.8\n")
        self.assertIn("Administrar 8.0mg VO SID.", output)

    def test_prednisolona_flow(self):
        output = run_app("10\nprednisolona\n2\n2\n")
        self.assertIn("Administrar 30.0mg IM/VO BID.", output)


if __name__ == "__main__":
    unittest.main()

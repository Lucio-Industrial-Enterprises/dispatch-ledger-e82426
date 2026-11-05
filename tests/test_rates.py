import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (preserved behaviour)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        """Explicitly passing service='standard' matches the default."""
        self.assertEqual(shipping_quote(2, "local", "standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", "standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # ------------------------------------------------------------------
    # Express service
    # ------------------------------------------------------------------
    def test_express_rates(self):
        """Express adds a $7 surcharge over the standard rate."""
        self.assertEqual(shipping_quote(2, "local", "express"), 15.0)
        self.assertEqual(shipping_quote(2, "regional", "express"), 18.0)

    def test_express_different_weights(self):
        self.assertAlmostEqual(shipping_quote(5, "local", "express"), 19.5)
        self.assertAlmostEqual(shipping_quote(5, "regional", "express"), 22.5)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", "overnight")

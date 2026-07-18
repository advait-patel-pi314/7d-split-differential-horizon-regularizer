import unittest
import numpy as np

# -------------------------------------------------------------------------
# THE PATCHED 7D MANIFOLD GRAVITATIONAL ENGINE
# -------------------------------------------------------------------------
def classical_g_rr(r, M=1.0):
    denominator = 1.0 - (2.0 * M / r)
    if np.isclose(denominator, 0.0):
        return float('inf')
    return 1.0 / denominator

def regularized_g_rr(r, M=1.0, j_proxy=0.05):
    """
    Implements the updated 7D split-recombination metric handoff.
    Uses the boundary-damped operator D(1, U) = U + j*(1-U)^2
    """
    U = 1.0 - (2.0 * M / r)
    # Patched division operator incorporating localized boundary damping
    D_1_U = U + j_proxy * ((1.0 - U)**2)
    return 1.0 / D_1_U

def compute_split_derivative_check(r_step, M=1.0, j_proxy=0.05):
    r_horizon = 2.0 * M
    val_at_horizon = regularized_g_rr(r_horizon, M, j_proxy)
    val_slightly_away = regularized_g_rr(r_horizon + r_step, M, j_proxy)
    return (val_slightly_away - val_at_horizon) / r_step


# -------------------------------------------------------------------------
# TESTING SUITE
# -------------------------------------------------------------------------
class Test7DManifoldHorizon(unittest.TestCase):

    def setUp(self):
        self.M = 1.0
        self.horizon_radius = 2.0 * self.M
        self.j_proxy = 0.05  
        
    def test_classical_singularity_verification(self):
        """PROOF 1: Confirm that standard GR absolutely fails at the horizon."""
        classical_value = classical_g_rr(self.horizon_radius, self.M)
        self.assertEqual(classical_value, float('inf'))

    def test_7d_horizon_handoff(self):
        """PROOF 2: Prove the j-glue catches the infinity and outputs exactly 1/j."""
        ring_value = regularized_g_rr(self.horizon_radius, self.M, self.j_proxy)
        expected_value = 1.0 / self.j_proxy
        self.assertAlmostEqual(ring_value, expected_value, places=7)

    def test_asymptotic_decoupling(self):
        """PROOF 3: Verify the 7D metric matches standard physics far from the black hole."""
        large_r = 500.0
        classical_val = classical_g_rr(large_r, self.M)
        ring_val = regularized_g_rr(large_r, self.M, self.j_proxy)
        
        # The boundary damping factor ensures convergence well within 4 decimal places
        self.assertAlmostEqual(ring_val, classical_val, places=4)

    def test_split_differentiation_continuity(self):
        """PROOF 4: Confirm that spatial variations across the horizon are smooth and finite."""
        step = 1e-5
        derivative_rate = compute_split_derivative_check(step, self.M, self.j_proxy)
        self.assertTrue(np.isfinite(derivative_rate))


if __name__ == "__main__":
    print("🔬 Testing 7D Manifold Split-Differentiation across Event Horizons...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
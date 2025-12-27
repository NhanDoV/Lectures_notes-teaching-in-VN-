import numpy as np
import math
import random
import itertools
from typing import Tuple, List, Dict

class Distribution:
    """
        Sampling primitives for Monte Carlo simulations.

        This class ONLY generates random samples.
        It contains no problem-specific logic.
    """

    # =========================
    # Continuous distributions
    # =========================

    @staticmethod
    def uniform(a: float = 0.0, b: float = 1.0) -> float:
        """Sample from Uniform(a, b)."""
        return random.uniform(a, b)

    @staticmethod
    def uniform_vec(a: float, b: float, size: int):
        """Vectorized Uniform(a, b)."""
        return np.random.uniform(a, b, size)

    # =========================
    # Bernoulli / Coin
    # =========================

    @staticmethod
    def fair_coin() -> int:
        """Return 1 (H) or 0 (T) with probability 1/2."""
        return 1 if random.random() < 0.5 else 0

    @staticmethod
    def biased_coin(p: float) -> int:
        """Bernoulli(p)."""
        return 1 if random.random() < p else 0

    @staticmethod
    def von_neumann_fair_coin(p: float) -> int:
        """
        Generate a fair coin from a biased coin using
        the Von Neumann trick.
        """
        while True:
            a = Distribution.biased_coin(p)
            b = Distribution.biased_coin(p)
            if a == 1 and b == 0:
                return 1
            if a == 0 and b == 1:
                return 0

    # =========================
    # Discrete distributions
    # =========================

    @staticmethod
    def dice() -> int:
        """Roll a fair six-sided die."""
        return random.randint(1, 6)

    @staticmethod
    def choice(items: List, probs: List[float]):
        """Discrete random choice."""
        return np.random.choice(items, p=probs)

    # =========================
    # Geometry samplers
    # =========================

    @staticmethod
    def point_in_circle(radius: float = 1.0) -> Tuple[float, float]:
        """
        Uniform random point inside a circle.
        """
        r = np.sqrt(random.random()) * radius
        theta = random.uniform(0, 2 * np.pi)
        return r * np.cos(theta), r * np.sin(theta)

    @staticmethod
    def point_in_triangle(
        A: Tuple[float, float],
        B: Tuple[float, float],
        C: Tuple[float, float],
    ) -> Tuple[float, float]:
        """
        Uniform random point inside triangle ABC.
        """
        u, v = random.random(), random.random()
        if u + v > 1:
            u, v = 1 - u, 1 - v

        x = A[0] + u * (B[0] - A[0]) + v * (C[0] - A[0])
        y = A[1] + u * (B[1] - A[1]) + v * (C[1] - A[1])
        return x, y

    # =========================
    # Geometry helpers
    # =========================

    @staticmethod
    def distance(p: Tuple[float, float], q: Tuple[float, float]) -> float:
        """Euclidean distance."""
        return np.hypot(p[0] - q[0], p[1] - q[1])

    @staticmethod
    def distance_point_to_line(
        P: Tuple[float, float],
        A: Tuple[float, float],
        B: Tuple[float, float],
    ) -> float:
        """Distance from point P to line AB."""
        x0, y0 = P
        x1, y1 = A
        x2, y2 = B
        num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        den = np.hypot(y2 - y1, x2 - x1)
        return num / den

    # =========================
    # Random walk
    # =========================

    @staticmethod
    def random_walk_step(
        pos: Tuple[int, int],
        step: Tuple[int, int],
        directions: List[str],
        probs: List[float],
    ) -> Tuple[int, int]:
        """
        One step of a constrained random walk.
        """
        x, y = pos
        dx, dy = step
        move = np.random.choice(directions, p=probs)

        if move == "L":
            return x - dx, y
        if move == "R":
            return x + dx, y
        if move == "U":
            return x, y + dy
        if move == "D":
            return x, y - dy

        raise ValueError("Invalid direction")

class FiniteProbModels:
    """
    Finite / discrete probability models solved via Monte Carlo simulation.

    This class covers problems involving:
    - coin tossing (fair / biased)
    - dice
    - finite stopping-time events
    - discrete random experiments

    Covered problems from original list:
        #1, #2, #4, #5, #14, #18, #20
    """

    # =====================================================
    # Coin models
    # =====================================================

    @staticmethod
    def simulate_event_from_biased_coin(
        q: float, prob_head: float, n_bits: int
    ) -> int:
        """
        Simulate a Bernoulli(q) event using a biased coin with P(H)=prob_head
        via Von Neumann + binary expansion.

        Returns:
            1 with probability approx q, else 0.
        """

        def unfair_coin():
            return 1 if random.random() < prob_head else 0

        def fair_coin():
            while True:
                a, b = unfair_coin(), unfair_coin()
                if a != b:
                    return a

        u = 0.0
        for i in range(n_bits):
            u += fair_coin() * (0.5 ** (i + 1))

        return int(u < q)

    @staticmethod
    def expected_time_for_pattern(pattern: str, n_sims: int) -> float:
        """
        Expected number of fair-coin tosses until a given pattern appears.
        """
        total = 0
        for _ in range(n_sims):
            seq, cnt = "", 0
            while pattern not in seq:
                seq += "H" if random.random() < 0.5 else "T"
                cnt += 1
            total += cnt
        return total / n_sims

    # =====================================================
    # Dice
    # =====================================================

    @staticmethod
    def prob_strictly_increasing_dice(n_dice: int, n_sims: int) -> float:
        """
        Probability that dice results are strictly increasing.
        """
        cnt = 0
        for _ in range(n_sims):
            rolls = [random.randint(1, 6) for _ in range(n_dice)]
            if all(rolls[i] < rolls[i + 1] for i in range(n_dice - 1)):
                cnt += 1
        return cnt / n_sims

    # =====================================================
    # Stick breaking
    # =====================================================

    @staticmethod
    def prob_triangle_from_broken_stick(
        n_outer: int, n_inner: int
    ) -> float:
        """
        Probability that a randomly broken stick forms a triangle.
        """
        probs = []
        for _ in range(n_outer):
            cnt = 0
            for _ in range(n_inner):
                a, b = sorted(np.random.rand(2))
                x = a
                y = b - a
                z = 1 - b
                if x + y > z and x + z > y and y + z > x:
                    cnt += 1
            probs.append(cnt / n_inner)
        return float(np.mean(probs))

    # =====================================================
    # Expected value / stopping games (finite)
    # =====================================================

    @staticmethod
    def biased_coin_wealth(
        prob_head: float,
        n_tosses: int,
        n_sims: int,
        gain: int = 1,
        loss: int = 100,
    ) -> Dict[str, float]:
        """
        Expected wealth from biased coin tossing with asymmetric payoff.
        """
        wealth = np.zeros(n_sims)
        for i in range(n_sims):
            tosses = np.random.rand(n_tosses)
            wealth[i] = np.sum(
                np.where(tosses < prob_head, gain, -loss)
            )
        return {
            "mean": float(np.mean(wealth)),
            "std": float(np.std(wealth)),
        }

    @staticmethod
    def expected_apples_left(
        n_sims: int, n_red: int = 60, n_green: int = 4
    ) -> float:
        """
        Expected number of apples remaining when all green apples are removed.
        """
        remaining = []
        for _ in range(n_sims):
            r, g = n_red, n_green
            while g > 0:
                if random.random() < g / (r + g):
                    g -= 1
                else:
                    r -= 1
            remaining.append(r)
        return sum(remaining) / n_sims

    @staticmethod
    def three_riflemen_prob(n_sims: int = 100_000) -> Dict[str, float]:
        """
        Probability each rifleman wins in the classic three-riflemen problem.
        """

        wins = {0: 0, 1: 0, 2: 0}

        for _ in range(n_sims):
            turn = 0
            while True:
                if random.random() < 0.5:
                    wins[turn % 3] += 1
                    break
                turn += 1

        return {
            "P(A)": wins[0] / n_sims,
            "P(B)": wins[1] / n_sims,
            "P(C)": wins[2] / n_sims,
        }

class GeometricProbability:
    """
    Geometric probability problems solved via Monte Carlo simulation.

    This class covers the following problems from the original list:
        - Problem 6   : Distance distribution in a circle
        - Problem 7   : Distance to center or boundary in a circle
        - Problem 8   : Distance between two random points in a circle
        - Problem 9   : Probability distance < R/2 in a circle
        - Problem 15  : Expected |X - Y| on a line segment
        - Problem 23  : Expected sum of perpendicular distances in a triangle
    """

    @staticmethod
    def distance_from_center_circle(n_sims: int, radius: float = 1.0):
        """
        Median and mean distance of a random point to the center of a circle.
        """
        dists = []

        for _ in range(n_sims):
            x, y = Distribution.point_in_circle(radius)
            dists.append(np.hypot(x, y))

        return {
            "median": float(np.median(dists)),
            "mean": float(np.mean(dists)),
        }

    @staticmethod
    def critical_distance_circle(
        n_sims: int,
        radius: float,
        coef: float,
        inner_trials: int = 5000,
    ) -> float:
        """
        Find R such that coef * P(D > R) < P(D < R),
        where D = min(distance to center, distance to boundary).
        """
        R_vals = []

        target = coef / (coef + 1)

        for _ in range(n_sims):
            D = []
            for _ in range(inner_trials):
                x, y = Distribution.point_in_circle(radius)
                d1 = np.hypot(x, y)
                d2 = radius - d1
                D.append(min(d1, d2))

            D = np.array(D)

            lo, hi = 0.0, radius / 2
            for _ in range(50):
                mid = (lo + hi) / 2
                if np.mean(D < mid) > target:
                    hi = mid
                else:
                    lo = mid

            R_vals.append(hi * 100)  # cm

        return float(np.mean(R_vals))

    @staticmethod
    def expected_distance_two_points_circle(
        n_sims: int, radius: float = 1.0
    ) -> float:
        dists = []

        for _ in range(n_sims):
            x1, y1 = Distribution.point_in_circle(radius)
            x2, y2 = Distribution.point_in_circle(radius)
            dists.append(np.hypot(x1 - x2, y1 - y2))

        return float(np.mean(dists))

    @staticmethod
    def prob_distance_less_than_half_radius(
        n_sims: int, radius: float = 1.0
    ) -> float:
        cnt = 0

        for _ in range(n_sims):
            x1, y1 = Distribution.point_in_circle(radius)
            x2, y2 = Distribution.point_in_circle(radius)
            if np.hypot(x1 - x2, y1 - y2) < radius / 2:
                cnt += 1

        return cnt / n_sims

    @staticmethod
    def expected_absolute_difference_line(
        L: float, n_sims: int
    ) -> float:
        diffs = []

        for _ in range(n_sims):
            x = np.random.uniform(0, L)
            y = np.random.uniform(0, L)
            diffs.append(abs(x - y))

        return float(np.mean(diffs))

    @staticmethod
    def expected_sum_perpendicular_distances_triangle(
        n_sims: int
    ) -> float:
        A = (0.0, 0.0)
        B = (60.0, 0.0)
        C = (0.0, 45.0)

        def dist_point_line(P, X, Y):
            num = abs(
                (Y[1] - X[1]) * P[0]
                - (Y[0] - X[0]) * P[1]
                + Y[0] * X[1]
                - Y[1] * X[0]
            )
            den = np.hypot(Y[1] - X[1], Y[0] - X[0])
            return num / den

        total = 0.0
        for _ in range(n_sims):
            P = Distribution.point_in_triangle(A, B, C)
            total += (
                dist_point_line(P, A, B)
                + dist_point_line(P, B, C)
                + dist_point_line(P, C, A)
            )

        return total / n_sims

class GeometricProbability:
    """
        Geometric probability problems solved via Monte Carlo simulation.

        Problems covered (from the original 23):
            - #6  Median / mean distance in a circle
            - #7  Distance to center or circumference
            - #8  Expected distance between two random points in a circle
            - #9  Probability distance < R/2
            - #15 Expected |X - Y| on a line segment
            - #23 Expected sum of perpendicular distances in a triangle
    """

    # ---------- Circle ----------

    @staticmethod
    def median_distance_in_circle(n_sims: int, radius: float = 1.0):
        dists = []
        for _ in range(n_sims):
            x, y = Distribution.point_in_circle(radius)
            dists.append(math.hypot(x, y))

        return {
            "median": float(np.median(dists)),
            "mean": float(np.mean(dists)),
        }

    @staticmethod
    def expected_distance_two_points_in_circle(
        n_sims: int, radius: float = 1.0
    ) -> float:
        dists = []
        for _ in range(n_sims):
            x1, y1 = Distribution.point_in_circle(radius)
            x2, y2 = Distribution.point_in_circle(radius)
            dists.append(math.hypot(x1 - x2, y1 - y2))
        return float(np.mean(dists))

    @staticmethod
    def prob_distance_less_than_half_radius(
        n_sims: int, radius: float = 1.0
    ) -> float:
        cnt = 0
        for _ in range(n_sims):
            x1, y1 = Distribution.point_in_circle(radius)
            x2, y2 = Distribution.point_in_circle(radius)
            if math.hypot(x1 - x2, y1 - y2) < radius / 2:
                cnt += 1
        return cnt / n_sims
    
    # ---------- Line ----------

    @staticmethod
    def expected_absolute_difference(
        L: float = 60.0, n_sims: int = 100_000
    ) -> float:
        total = 0.0
        for _ in range(n_sims):
            x = np.random.uniform(0, L)
            y = np.random.uniform(0, L)
            total += abs(x - y)
        return total / n_sims
    
    # ---------- Triangle ----------

    @staticmethod
    def expected_sum_perpendicular_distances_triangle(
        n_sims: int,
    ) -> float:
        A = (0.0, 0.0)
        B = (60.0, 0.0)
        C = (0.0, 45.0)

        def dist_point_to_line(P, X, Y):
            x0, y0 = P
            x1, y1 = X
            x2, y2 = Y
            num = abs(
                (y2 - y1) * x0
                - (x2 - x1) * y0
                + x2 * y1
                - y2 * x1
            )
            den = math.hypot(y2 - y1, x2 - x1)
            return num / den

        total = 0.0
        for _ in range(n_sims):
            P = Distribution.point_in_triangle(A, B, C)
            total += (
                dist_point_to_line(P, A, B)
                + dist_point_to_line(P, B, C)
                + dist_point_to_line(P, C, A)
            )

        return total / n_sims

class RandomWalkLattice:
    """
    Random walk and lattice-based stochastic process problems.

    Covers Problems:
        - #11 Expected steps to wall
        - #12 Probability reach corner
        - #13 Expected number of turns
        - #21 Waffles the Street Cat
        - #22 Fifty Ants
    """

    # ============================================================
    # Problem 11
    @staticmethod
    def expected_steps_to_wall(m: int, n: int, n_sims: int) -> float:
        """
        Expected number of steps until reaching x=m or y=n,
        moving only Right or Up with equal probability.
        """
        steps = []

        for _ in range(n_sims):
            x = y = 0
            cnt = 0
            while x < m and y < n:
                if random.random() < 0.5:
                    x += 1
                else:
                    y += 1
                cnt += 1
            steps.append(cnt)

        return float(np.mean(steps))

    # ============================================================
    # Problem 12
    @staticmethod
    def probability_reach_corner(m: int, n: int, n_sims: int) -> float:
        """
        Probability that a random walk reaches (m, n)
        before crossing outside the lattice.
        """
        success = 0

        for _ in range(n_sims):
            x = y = 0
            while True:
                if random.random() < 0.5:
                    x += 1
                else:
                    y += 1

                if x == m and y == n:
                    success += 1
                    break
                if x > m or y > n:
                    break

        return success / n_sims

    # ============================================================
    # Problem 13
    @staticmethod
    def expected_number_of_turns(m: int, n: int, n_sims: int) -> float:
        """
        Expected number of direction changes (turns)
        until reaching or exceeding (m, n).
        """
        turns_all = []

        for _ in range(n_sims):
            x = y = 0
            prev_move = None
            turns = 0

            while x < m or y < n:
                move = "R" if random.random() < 0.5 else "U"

                if prev_move and move != prev_move:
                    turns += 1

                if move == "R":
                    x += 1
                else:
                    y += 1

                prev_move = move

            turns_all.append(turns)

        return float(np.mean(turns_all))

    # ============================================================
    # Problem 21
    @staticmethod
    def waffles_street_cat(n_houses: int, days: int) -> float:
        """
        Probability that Waffles the Cat is at house 1 after 'days' days.
        1D symmetric random walk with reflecting boundaries.
        """
        prev = np.zeros(n_houses + 1)
        curr = np.zeros(n_houses + 1)

        prev[1] = 1.0  # start at house 1

        for _ in range(days):
            curr[:] = 0.0
            for i in range(1, n_houses + 1):
                if prev[i] == 0:
                    continue

                if i == 1:
                    curr[2] += prev[1]
                elif i == n_houses:
                    curr[n_houses - 1] += prev[n_houses]
                else:
                    curr[i - 1] += 0.5 * prev[i]
                    curr[i + 1] += 0.5 * prev[i]

            prev, curr = curr, prev

        return prev[1]

    # ============================================================
    # Problem 22
    @staticmethod
    def fifty_ants(n_ants: int = 50, n_sims: int = 1000) -> float:
        """
        Expected time until the last ant falls off the stick.
        """
        times = []

        for _ in range(n_sims):
            max_time = 0.0
            for _ in range(n_ants):
                x = random.random()   # position in [0,1]
                t = x if random.random() < 0.5 else 1 - x
                max_time = max(max_time, t)
            times.append(max_time)

        return float(np.mean(times))

class ExpectedValGames:
    """
    Expected value and payoff-based stochastic games.

    Covers problems:
        - #14: Expected wealth from biased coin tossing
        - #17: Expected number of strong bridges crossed
        - #20: Three riflemen expected winnings
    """

    # --------------------------------------------------
    # Problem 14
    # --------------------------------------------------
    @staticmethod
    def biased_coin_wealth(
        prob_head: float,
        n_tosses: int,
        n_sims: int
    ) -> dict:
        """
        Expected wealth from repeated biased coin tosses.

        +1 for Head, -100 for Tail.
        """
        if not (0 < prob_head < 1):
            raise ValueError("prob_head must be in (0,1)")

        wealth = np.zeros(n_sims)

        for i in range(n_sims):
            tosses = np.random.rand(n_tosses)
            wealth[i] = np.sum(np.where(tosses < prob_head, 1, -100))

        return {
            "empirical_mean": float(np.mean(wealth)),
            "empirical_std": float(np.std(wealth)),
            "theoretical_mean": n_tosses * (prob_head - 100 * (1 - prob_head)),
        }

    # --------------------------------------------------
    # Problem 17
    # --------------------------------------------------
    @staticmethod
    def expected_strong_bridges(
        n_islands: int,
        n_sims: int
    ) -> dict:
        """
        Expected number of strong bridges crossed before reaching final island.
        """

        def one_run():
            remaining = [2] * (n_islands - 1)
            pos = 1
            strong_count = 0

            while pos < n_islands:
                idx = pos - 1

                if remaining[idx] == 1:
                    strong_count += 1
                    pos += 1
                else:
                    if np.random.rand() < 0.5:   # strong
                        strong_count += 1
                        pos += 1
                    else:                         # weak
                        remaining[idx] = 1
                        pos = 1

            return strong_count

        res = [one_run() for _ in range(n_sims)]

        return {
            "expected_strong": float(np.mean(res)),
            "std": float(np.std(res)),
        }

    # --------------------------------------------------
    # Problem 20
    # --------------------------------------------------
    @staticmethod
    def three_riflemen(
        prize: int,
        n_sims: int
    ) -> dict:
        """
        Expected winnings in the three-riflemen shooting game.
        """

        wins = {0: 0, 1: 0, 2: 0}

        for _ in range(n_sims):
            turn = 0
            while True:
                if np.random.rand() < 0.5:
                    wins[turn % 3] += 1
                    break
                turn += 1

        pA = wins[0] / n_sims
        pB = wins[1] / n_sims
        pC = wins[2] / n_sims

        return {
            "P(A)": pA,
            "P(B)": pB,
            "P(C)": pC,
            "expected_A": prize * pA,
            "theoretical_P(A)": 4 / 7,
        }

class Combinatorics:
    """
    Combinatorial counting problems.

    This class solves:
        - Problem 10: Ant paths with exactly two turns
        - Problem 19: Round-table seating with gender constraints
    """

    @staticmethod
    def ant_paths_with_two_turns(m: int, n: int) -> int:
        """
        Count the number of paths from (0,0) to (m,n)
        using only Right (R) and Up (U) moves
        with exactly two direction changes.

        Solves Problem #10.
        """
        total_steps = m + n
        count = 0

        for r_positions in itertools.combinations(range(total_steps), m):
            path = ["U"] * total_steps
            for i in r_positions:
                path[i] = "R"

            # count turns
            turns = sum(
                path[i] != path[i + 1]
                for i in range(len(path) - 1)
            )

            if turns == 2:
                count += 1

        return count

    @staticmethod
    def round_table_no_adjacent_same_gender(n: int) -> float:
        """
        Probability that no two persons of the same gender
        sit next to each other around a round table.

        There are n men and n women.

        Solves Problem #19.
        """
        men = [f"M{i}" for i in range(n)]
        women = [f"W{i}" for i in range(n)]

        valid = 0
        total = math.factorial(2 * n - 1)

        gender_pattern = ["M" if i % 2 == 0 else "W" for i in range(2 * n)]

        for men_perm in itertools.permutations(men):
            for women_perm in itertools.permutations(women):
                arrangement = []
                mi = wi = 0

                for g in gender_pattern:
                    if g == "M":
                        arrangement.append(men_perm[mi])
                        mi += 1
                    else:
                        arrangement.append(women_perm[wi])
                        wi += 1

                valid += 1

        return valid / total

        # =====================================================
        # Combinatorics
        # -----------------------------------------------------
        # Solved problems:
        #   - #10: Ant paths with exactly two turns
        #   - #19: Round-table seating (men / women)
        # =====================================================

class MarkovDPModels:
    """
    Markov chains and dynamic programming models.

    Covers problems:
        - #11 Expected steps to wall (DP)
        - #12 Probability reach corner (absorbing Markov)
        - #21 Waffles the Cat (Markov chain on line)
    """

    # -------------------------------------------------
    # Problem 21: Waffles the Cat
    # -------------------------------------------------
    @staticmethod
    def waffles_cat_prob_return(
        n_houses: int,
        days: int,
        start_house: int = 1,
        target_house: int = 1,
    ) -> float:
        """
        Probability that Waffles is at target_house after `days` days.

        Markov chain on a line with reflecting boundaries.

        State: house index ∈ {1,...,n_houses}
        Transition:
            - middle house: 1/2 left, 1/2 right
            - boundary: forced inward
        """

        prev = np.zeros(n_houses + 1)
        curr = np.zeros(n_houses + 1)

        prev[start_house] = 1.0

        for _ in range(days):
            curr[:] = 0.0
            for i in range(1, n_houses + 1):
                if prev[i] == 0:
                    continue

                if i == 1:
                    curr[2] += prev[i]
                elif i == n_houses:
                    curr[n_houses - 1] += prev[i]
                else:
                    curr[i - 1] += 0.5 * prev[i]
                    curr[i + 1] += 0.5 * prev[i]

            prev, curr = curr, prev

        return prev[target_house]

    # -------------------------------------------------
    # Problem 12: Probability reach corner (absorbing)
    # -------------------------------------------------
    @staticmethod
    def prob_reach_corner_dp(m: int, n: int) -> float:
        """
        Probability a random walker starting at (0,0) reaches (m,n)
        before exiting the grid.

        DP with absorbing boundaries.

        Transition:
            (x,y) -> (x+1,y) or (x,y+1) with prob 1/2
        """

        dp = np.zeros((m + 1, n + 1))
        dp[m, n] = 1.0   # absorbing success state

        # backward DP
        for x in range(m, -1, -1):
            for y in range(n, -1, -1):
                if (x, y) == (m, n):
                    continue
                if x == m or y == n:
                    dp[x, y] = 0.0
                else:
                    dp[x, y] = 0.5 * dp[x + 1, y] + 0.5 * dp[x, y + 1]

        return dp[0, 0]

    # -------------------------------------------------
    # Problem 11: Expected steps to wall (DP)
    # -------------------------------------------------
    @staticmethod
    def expected_steps_to_wall_dp(m: int, n: int) -> float:
        """
        Expected number of steps until hitting x=m or y=n.

        Let E[x,y] = expected steps from (x,y).

        Recurrence:
            E[x,y] = 1 + 0.5 * E[x+1,y] + 0.5 * E[x,y+1]
        Boundary:
            E[x,y] = 0 if x=m or y=n
        """

        E = np.zeros((m + 1, n + 1))

        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                E[x, y] = 1 + 0.5 * E[x + 1, y] + 0.5 * E[x, y + 1]

        return E[0, 0]
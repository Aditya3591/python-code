import random

class CouponSimulator:
    @staticmethod
    def generate_coupon_numbers(N):
        return list(range(1, N + 1))

    @staticmethod
    def generate_random_coupon(N):
        return random.randint(1, N)

    @staticmethod
    def get_random_coupon_count(N):
        coupon_numbers = CouponSimulator.generate_coupon_numbers(N)
        distinct_coupons = set()
        random_count = 0

        while len(distinct_coupons) < N:
            random_coupon = CouponSimulator.generate_random_coupon(N)
            random_count += 1
            distinct_coupons.add(random_coupon)

        return random_count

N = int(input("Enter the number of distinct coupon numbers: "))


random_count = CouponSimulator.get_random_coupon_count(N)

print(f"Total random numbers needed to have all distinct numbers: {random_count}")

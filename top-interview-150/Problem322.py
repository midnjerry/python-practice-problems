# https://leetcode.com/problems/coin-change/
class Problem322:
    def coinChange(self, coins: list[int], amount:int) -> int:
        minAmount = -1
        for i in range(len(coins)):
            num = self.findMinAmount(coins, amount-coins[i], 0)
            if (num > -1):
                if (minAmount == -1 or num < minAmount):
                    minAmount = num

        return minAmount


    def findMinAmount(self, coins: list[int], amount: int, count: int) -> int:
        if(amount == 0):
            return count
        if (amount < 0):
            return -1

        minAmount = -1
        for i in range(len(coins)):
            num = self.findMinAmount(coins, amount-coins[i], count + 1)
            if (num > -1):
                if (minAmount == -1 or num < minAmount):
                    minAmount = num

        return minAmount
        
if __name__ == '__main__':
    solution = Problem322()    
    print(f'[1,2,5], 11 (expected 3): {solution.coinChange([1,2,5], 11)}')
    print(f'[2], 3 (expected -1): {solution.coinChange([2], 3)}')
    print(f'[1], 0 (expected 0): {solution.coinChange([1], 0)}')
    
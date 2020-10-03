"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""
if __name__ == '__main__':
    arr=[]
    sma=-200
    n = int(input())
    arr=input().split()
    for i in range (len(arr)):
        arr[i]=int(arr[i])
    ma=max(arr)
    for i in range (len(arr)):
        if(sma<arr[i])and(arr[i]!=ma):
            sma=arr[i]
    print(sma)

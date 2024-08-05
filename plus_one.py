# digits=list(map(int,input().split()))
# sum=''
# new_new_sum=[]
# for i in digits:
#     str1=str(i)
#     sum=sum+str1
# new_sum=int(sum)+1
# print(new_sum)
# for j in str(new_sum):
#     new_new_sum.append(int(j))
# print(new_new_sum)


##using O(n) complexity
digits=list(map(int,input().split()))
new_digits=''.join(map(str,digits))
new_sum=int(new_digits)+1
final_list=list(map(int,str(new_sum)))
print(final_list)
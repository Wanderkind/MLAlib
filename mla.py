
def zero_mat(n,p):
    '''
    영행렬 생성
    입력값: 생성하고자 할 영행렬의 크기 n행, p열
    출력값: n×p 영행렬 Z
    '''
    Z=[]
    for i in range(n):
        row=[]
        for j in range(p):
            Z.append(row)
    return Z


def deepcopy(A):
    '''
    깊은 복사(deepcopy) 구현
    입력값: 깊은 복사를 하고자 하는 행렬 리스트 A
    출력값: 갚은 복사 된 결과 행렬 리스트 res
    '''
    if type(A[0])==list:
        n=len(A)
        p=len(A[0])
        res=zero_mat(n,p)
        for i in range(n):
            for j in range(p):
                res[i][j]=A[i][j]
        return res
    else:
        n=len(A)
        res=[]
        for i in range(n):
            res.append(A[i])
        return res


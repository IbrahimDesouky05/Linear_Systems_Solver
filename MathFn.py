import gauss_elimination as ge
import lu_decomposition as lu
import jacobi_method as jm
import gauss_seidel_method as gsm
import timeit

def all_math_functions(mat, vec, size, strt_vector = None):

    ans1 = ge.GaussElimination(mat,vec)
    ans2 = lu.lu(mat,size,vec)
    ans3, i1 = gsm.gauss_seidel_method(mat,vec,ans1,strt_vector)
    ans4, i2 = jm.jacobian_method(mat,vec,ans1,strt_vector)

    t1 = timeit.timeit(lambda: ge.GaussElimination(mat,vec),number=1000)
    t2 = timeit.timeit(lambda: lu.lu(mat,size,vec), number=1000)
    t3 = timeit.timeit(lambda: gsm.gauss_seidel_method(mat,vec,ans1,strt_vector), number=1) * 1000
    t4 = timeit.timeit(lambda: jm.jacobian_method(mat,vec,ans1,strt_vector), number=1) * 1000

    ans1 = [f"{x:.10g}" for x in ans1]
    ans2 = [f"{x:.10g}" for x in ans2]
    ans3 = [f"{x:.10g}" for x in ans3]
    ans4 = [f"{x:.10g}" for x in ans4]

    t1 = format(t1, ".10f")
    t2 = format(t2, ".10f")
    t3 = format(t3, ".10f")
    t4 = format(t4, ".10f")

    #print(ans1, t1, ans2, t2, ans3, i1, t3, ans4, i2, t4)      # Used to debug

    return ans1, ans2, ans3, ans4, i1, i2, t1, t2, t3, t4

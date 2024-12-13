import input_handler as ih
import gauss_elimination as ge
import lu_decomposition as lu
import jacobi_method as jm
import gauss_seidel_method as gsm

mat,size = ih.InputMatrix()
vec = ih.entryVector()
iterations = ih.iterationNumber()
gs_vector = ih.gs_vector()
ans1 = ge.GaussElimination(mat,vec)
ans2 = lu.lu(mat,size,vec)
ans3 = jm.jacobian_method(mat,vec,iterations)
ans4 = gsm.gauss_seidel_method(mat,vec,iterations,gs_vector)

print(ans1,"\n",ans2,"\n",ans3,"\n",ans4)
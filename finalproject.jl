using LinearAlgebra

b = [
    0 1 1 1 0;
    0 0 1 0 0;
    0 0 0 1 1;
    0 0 0 0 0;
    1 1 0 0 0
]

a = [
    0 1 1;
    0 0 1;
    1 0 0
]

at = a'

#=
display(a)
println()
display(a')
=#

authValMat = at * a
hubValMat = a * at

#=
5×5 Matrix{Int64}:
 1  1  0  0  0
 1  2  1  1  0
 0  1  2  1  0
 0  1  1  2  1
 0  0  0  1  1
5×5 Matrix{Int64}:
 3  1  1  0  1
 1  1  0  0  0
 1  0  2  0  0
 0  0  0  0  0
 1  0  0  0  2
 =#

authValEV = eigen(authValMat)
tmp = argmax(authValEV.values)
authVals = authValEV.vectors[:, tmp]
hubValEV = eigen(hubValMat)
tmp = argmax(hubValEV.values)
hubVals = hubValEV.vectors[:, tmp]

println()
print(reverse(sortperm(authVals)))
print(reverse(sortperm(hubVals)))

# [2 4 3 1 5]
# [4 2 3 5 1]

#=
print(authValEV)
println()
print(sortperm(authValEV))
println()
println()
print(hubValEV)
println()
print(sortperm(hubValEV))
=#
#=
[3.9359938464855304e-17, 0.32486912943335394, 1.4608111271891102, 2.0000000000000004, 4.214319743377534]
[1, 2, 3, 4, 5]

[0.0, 0.3248691294333543, 1.4608111271891109, 1.9999999999999996, 4.214319743377534]
[1, 2, 3, 4, 5]
=#

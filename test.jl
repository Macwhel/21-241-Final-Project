using Plots

v=[1;2];

w=[3,1];

#define two vectors v and w of your choosing (try different values!)

x=[a*v[1] + (1-a)*w[1] for a = -5 : 0.1 : 5];

#vector of x-coordinates of the affine combinations

y=[a*v[2] + (1-a)*w[2] for a = -5 : 0.1 : 5];

#vector of y-coordinates of the affine combinations

scatter(x, y, label="affine combinations")

#plot the affine combinations.


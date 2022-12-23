###############################################################################
# Script for generating estimated density 
###############################################################################

#xlist is the estimator for optimal decision variable theta^* after 200 iterations, using 200 independent runs
theta1= xlist[:,0] # the first dimension of the estimator of theta^*
theta2= xlist[:,1] # the second dimension of the estimator of theta^*

# [0.23173061, 0.26217133] is the optimal value of theta
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf
mean = np.sqrt(200)*(theta1-0.23173061).mean()

sigma= np.sqrt(200)*(theta1-0.23173061).std()
mean2= np.sqrt(200)*(theta2- 0.26217133).mean()

sigma2 = np.sqrt(200)*(theta2- 0.26217133).std()
plt.subplot(1,2,1)

sns.distplot(np.sqrt(200)*(theta1-0.23173061),bins=25)
sns.kdeplot(np.sqrt(200)*(theta1-0.23173061),kernel='gau',label='Empirical density of $\sqrt{t}(w_{1t}-w^*_{1})$',color='blue')
plt.ylabel('Density of $\sqrt{t}(w_{1t}-w^*_{1})$')
x = np.arange(-4,6,0.05)
plt.plot(x,normfun(x,mean,sigma),label='Density of a normal distribution',color='red')
lgd = plt.legend(fontsize=16)
lines = lgd.get_lines()
plt.yticks([0,0.05,0.10,0.15,0.20])
plt.legend(lines, ["Empirical density of $\sqrt{t}(w_{1t}-w^*_{1})$",'Density of a normal distribution'], fontsize=5)
plt.subplot(1,2,2)

sns.distplot(np.sqrt(200)*(theta2-0.26217133),bins=25)
sns.kdeplot(np.sqrt(200)*(theta2-0.26217133),kernel='gau',label='Empirical density of $\sqrt{t}(w_{2t}-w^*_{2})$',color='blue')
plt.ylabel('Density of $\sqrt{t}(w_{2t}-w^*_{2})$')
x = np.arange(-4,6,0.05)
plt.plot(x,normfun(x,mean2,sigma2),label='Density of a normal distribution',color='red')
lgd = plt.legend(fontsize=16)
lines = lgd.get_lines()
plt.legend(lines, ["Empirical density of $\sqrt{t}(w_{2t}-w^*_{2})$",'Density of a normal distribution'], fontsize=5)

plt.subplots_adjust(wspace=0.75)

plt.savefig("clt_adjust.pdf",dpi=6000,bbox_inches = 'tight')

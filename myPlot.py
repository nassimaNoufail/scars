import numpy as np
import matplotlib.pyplot as plt


scarRed=[67, 71, 61, 102, 85, 70, 43, 65, 52, 31, 37, 35, 17, 39, 29, 41, 115, 13, 57]
normRedCan=[101, 110, 85, 149, 101, 117, 81, 98, 85, 122, 130, 127, 123, 100, 121, 75, 138, 101, 70]
normRedSticker=[110,93,99,133,92,129,100,101,85,100,131,135,112,89,112,114,111,85,62]


#ORIGIN
#'''
plt.figure(1)
scarMean=np.mean(scarRed)
x=np.arange(20)
x=x[1:]
y=scarRed
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim([0,150])
plt.xlabel('Image label',fontsize=15)
plt.ylabel('Redness',fontsize=15)
plt.title('Redness of scars before normalisation')
plt.plot(x,y,'r.',markersize=15,label='Scar')
plt.plot([1, 19], [scarMean, scarMean], 'k-', lw=2,label='Mean')
plt.legend(loc='upper right')
#'''

#COKE CAN
plt.figure(2)
canMean=np.mean(normRedCan)
x=np.arange(20)
x=x[1:]
y=normRedCan
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim([0,150])
plt.xlabel('Image label',fontsize=15)
plt.ylabel('Redness',fontsize=15)
plt.title('Redness of scars after normalisation with can')
plt.plot(x,y,'r.',markersize=15,label='Scar')
plt.plot([1, 19], [canMean, canMean], 'k-', lw=2,label='Mean')
plt.legend(loc='upper left')


#STICKER
plt.figure(3)
stickerMean=np.mean(normRedSticker)
x=np.arange(20)
x=x[1:]
y=normRedSticker
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim([0,150])
plt.xlabel('Image label',fontsize=15)
plt.ylabel('Redness',fontsize=15)
plt.title('Redness of scars after normalisation with sticker')
plt.plot(x,y,'r.',markersize=15,label='Scar')
plt.plot([1, 19], [stickerMean, stickerMean], 'k-', lw=2,label='Mean')
plt.legend(loc='upper right')


#STICKER + ORIGIN
plt.figure(4)
stickerMean=np.mean(normRedSticker)
x=np.arange(20)
x=x[1:]
y=normRedSticker
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.ylim([0,150])
plt.xlabel('Image label',fontsize=15)
plt.ylabel('Redness',fontsize=15)
plt.title('Redness of scars after normalisation with sticker')
plt.plot(x,y,'r.',markersize=15,label='Scar')
plt.plot(x,scarRed,'g+',markersize=15,label='Original Scar')
plt.plot([1, 19], [stickerMean, stickerMean], 'k-', lw=2,label='Mean')
plt.legend(loc='upper right')





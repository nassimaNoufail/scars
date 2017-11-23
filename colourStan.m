%close all
figure
im= imread('cokeCan.jpg');

subplot(2,2,1)%%%%%%%%%%%
imshow(im)
title('OG')


[TR,TC,lol]=size(im);

trueColour=244; %coke red

mim=im;
[imR,imC]=size(mim(:,:,1));
d=145;
f=160;
colour=0;
mim(:,1:d,:)=colour;
mim(:,TC-d:TC,:)=colour;

mim(1:f,:,:)=colour;
mim(TR-f:TR,:,:)=colour;



n=nnz(mim(:,:,1));

[row,col]=find(mim(:,:,1),1);

myRow=163;
myCol=146;
for i=1:175-163
    RGB([mim(myRow,myCol,1),mim(myRow,myCol,2),mim(myRow,myCol,3)]);
    myRow=myRow+1;
end
%{
for i=1:TC
    for j=1:TR
        differM(i,j)=double(RGB([mim(i,j,1),mim(i,j,2),mim(i,j,3)]));
    end
end
%}
%[aa,bb]=find(differM);



gim=redExtract(im,TR,TC);

subplot(2,2,2)%%%%%%%%%%
imshow(gim)

title('Red Extractor')
totalNonZ=nnz(gim(:,:,1));%total non zero entries
meanR=sum(sum(gim(:,:,1)))/totalNonZ;
diff=trueColour-meanR;

%mean2=sum(sum(gim(:,:,2)))/total;
%mean3=sum(sum(gim(:,:,3)))/total;


for i=1:TR
    for j=1:TC
        if gim(i,j,1)>10
            gim(i,j,1)=gim(i,j,1)+diff;
        end
    end
end

subplot(2,2,4)
imshow(gim)
title('Final')




function result=RGB(vec)
vec=num2cell(vec);
[R,G,B]=vec{:};%unpack
R=double(R);
G=double(G);
B=double(B);
result=(R-G)*(R-B);
end

function image=redExtract(image,TR,TC)

for i=1:TR
    for j=1:TC
        differM(i,j)=RGB([image(i,j,1),image(i,j,2),image(i,j,3)]);
    end
end

for i=1:TR
    for j=1:TC
        if differM(i,j)>12000
        	lol=0;
        else
            image(i,j,:)=0;
        end
    end
end
%figure
%imshow(image)
end
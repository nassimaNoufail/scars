close all
im= imread('cokeCan2.jpg');
[TC,TR,lol]=size(im);

mim=im;
[imR,imC]=size(mim(:,:,1));
d=145;
f=160;
colour=0;
mim(:,1:d,:)=colour;
mim(:,TR-d:TR,:)=colour;

mim(1:f,:,:)=colour;
mim(TC-f:TC,:,:)=colour;

%figure
%imshow(im)

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
[aa,bb]=find(differM);



gim=redExtract(im,TC,TR);
gim(:,:,1);
total=nnz(gim(:,:,1));
mean1=sum(sum(gim(:,:,1)))/total
mean2=sum(sum(gim(:,:,2)))/total
mean3=sum(sum(gim(:,:,3)))/total
figure
imshow(gim)
gim(:,:,1)=gim(:,:,1)+40;
figure
imshow(gim)
function result=RGB(vec)
vec=num2cell(vec);
[R,G,B]=vec{:};%unpack
R=double(R);
G=double(G);
B=double(B);
result=(R-G)*(R-B);
end

function image=redExtract(image,TC,TR)
for i=1:TC
    for j=1:TR
        differM(i,j)=RGB([image(i,j,1),image(i,j,2),image(i,j,3)]);
    end
end
%[aa,bb]=find(differM);
for i=1:TC
    for j=1:TR
        if differM(i,j)>10000
        	lol=0;
        else
            image(i,j,:)=0;
        end
    end
end
%figure
%imshow(image)
end
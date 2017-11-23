close all
im= imread('cokeCan.jpg');
mim=im;
[imR,imC]=size(mim(:,:,1));
d=145;
f=160;
colour=0;
mim(:,1:d,:)=colour;
mim(:,300-d:300,:)=colour;

mim(1:f,:,:)=colour;
mim(336-f:336,:,:)=colour;

figure
imshow(im)

n=nnz(mim(:,:,1));

[row,col]=find(mim(:,:,1),1);

myRow=163;
myCol=146;
for i=1:175-163
    RGB([mim(myRow,myCol,1),mim(myRow,myCol,2),mim(myRow,myCol,3)]);
    myRow=myRow+1;
end
%%{
for i=1:336
    for j=1:300
        differM(i,j)=double(RGB([mim(i,j,1),mim(i,j,2),mim(i,j,3)]));
    end
end
%}
[aa,bb]=find(differM);
[aa,bb];


redExtract(im)


function result=RGB(vec)
vec=num2cell(vec);
[R,G,B]=vec{:};%unpack
R=double(R);
G=double(G);
B=double(B);
result=(R-G)*(R-B);
end

function redExtract(image)
for i=1:336
    for j=1:300
        differM(i,j)=RGB([image(i,j,1),image(i,j,2),image(i,j,3)]);
    end
end
%[aa,bb]=find(differM);
for i=1:336
    for j=1:300
        if differM(i,j)>10000
        	lol=0;
        else
            image(i,j,:)=0;
        end
    end
end
figure
imshow(image)
end
close all
im= imread('cokeCan.jpg');
trueColour=244;
[TR,TC,lol]=size(im);

%figure
%imshow(im)
[im(150,150,1),im(150,150,2),im(150,150,3)]


gim=redExtract(im,TR,TC);

total=nnz(gim(:,:,1));
mean1=sum(sum(gim(:,:,1)))/total;
mean2=sum(sum(gim(:,:,2)))/total;
mean3=sum(sum(gim(:,:,3)))/total;

%figure
%imshow(gim)

gim(:,:,1)=gim(:,:,1)+(trueColour-mean1);
%figure
%imshow(gim)
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
%[aa,bb]=find(differM);
for i=1:TR
    for j=1:TC
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
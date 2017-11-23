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


imshow(im)

n=nnz(mim(:,:,1));

[row,col]=find(mim(:,:,1),1);


for i=1:336
    for j=1:300
        differM(i,j)=RGB([im(i,j,1),im(i,j,2),im(i,j,3)]);
    end
end
[aa,bb]=find(differM);
for i=1:336
    for j=1:300
        if differM(i,j)>240
        	lol=0;
        else
            im(i,j,:)=0;
        end
    end
end


%sum(sum(mim(:,:,1)))/n;
%sum(sum(mim(:,:,2)))/n;
%sum(sum(mim(:,:,3)))/n;

figure
imshow(im)


function result=RGB(vec)
vec=num2cell(vec);
[R,G,B]=vec{:};%unpack
result=(R-G)*(R-B);
end
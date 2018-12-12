function y = runflow(Image1,Image2, i)

% Read in 2 images
I1 = imread(Image1);
%I1 = imcrop(I1_ori,[1300 650 1285 1285]);

I2 = imread(Image2);
%I2 = imcrop(I2_ori,[1300 650 1285 1285]);

% convert to grayscale
frame1 = double(rgb2gray(I1));
frame2 = double(rgb2gray(I2));

% optical flow parameters
lambda = 10;  % you can try differnt value for different cases

% estimate optical flow using, this outputs a 2d array with u,v values for each point 
uv = estimateHSflow(frame1,frame2,lambda);

% warp frame2 to frame1 accroding to the estimated optical flow
[H, W, chs] = size(I2);
[x,y] = meshgrid(1:W,1:H);
x1 = x-uv(:,:,1);
y1 = y-uv(:,:,2);
warpimg2 = [];

for ch = 1:size(I2,3)
    warpimg2(:,:,ch) = interp2_bicubic(double(I2(:,:,ch)),x1,y1);
end

warpimg2(isnan(warpimg2)) = 0;

forecastname = str2double(regexp(Image2,'\d*','Match'));

RealNum = num2str(forecastname + i);

Final = ['forecast_DSC_',RealNum,'.jpg'];

imwrite(uint8(warpimg2),Final);

%I3_ori = imread('DSC_0126.JPG');
%I3 = imcrop(I3_ori,[1300 650 1285 1285]);
%figure,
%subplot(1,2,1), imshow(uint8(warpimg2)),title('Warped Image')
%subplot(1,2,2), imshow(rgb2gray(I3)),title('Actual Image')










%% Load in a single dicom file
I = dicomread('/MATLAB Drive/1340/L2-922021/pigdicom/1.3.12.2.1107.5.2.31.30831.20130403190751299695434.dcm');

figure(1)
subplot(1,2,1);
imshow(I,[min(I(:)), max(I(:))])

subplot(1,2,2);
fReal = (fftshift(fft2(I)));
fAbs = abs(fftshift(fft2(I)));
imshow(fAbs,[min(fAbs(:)), max(fAbs(:))])


%% Read entire stack
dicomlist = dir(['/MATLAB Drive/1340/L2-922021/pigdicom/','*.dcm']);
I_stack = zeros([size(I),numel(dicomlist)]);

for cnt = 1 : numel(dicomlist)
% for cnt = numel(dicomlist):-1:1
    I_stack(:,:,cnt) = flipud(dicomread(['/MATLAB Drive/1340/L2-922021/pigdicom/',dicomlist(cnt).name]));  
end

Islice = squeeze(I_stack(:, 256/2,:));
imshow(Islice',[min(Islice(:)), max(Islice(:))]);

%% Write vtk volume out
filename = "pigdicomstack_flippedZ.vtk";
Spacing = [1.5, 1.5, 4.5];
write_vtk_Volume(I_stack, Spacing, filename);

% Verify the export is complete: value count must equal nx*ny*nz.
expected = numel(I_stack);
txt = fileread(filename);
actual = numel(sscanf(txt(strfind(txt, 'LOOKUP_TABLE default') + 20 : end), '%g'));
fprintf('VTK export: expected %d values, wrote %d (%s)\n', ...
    expected, actual, string(actual == expected));


%% Try another writing method
filename = "pigdicomstack_flippedZ_1.vtk";
write_vtk_Volume(I_stack, Spacing, filename);
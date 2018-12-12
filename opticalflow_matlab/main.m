filePattern = fullfile('./', '*.jpg');
files = dir(filePattern);

imagename = {};

for i=1:length(files)
    filename = files(i);
    imagename = [imagename, filename.name];  
end

for i=1:(length(imagename)/2)
    runflow(imagename{1},imagename{i+1},i);    
end



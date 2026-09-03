function write_vtk_Volume(array, Spacing, filename)

%  write_vtk_Volume: Save a 3-D scalar array in VTK format.
%  write_vtk_Volume(array, Voxel_Spacing, filename) saves a 3-D array of any size with known Voxel_Spacing (1x3 vector) to filename in VTK format.
%
% Written by Prahlad G Menon, PhD

    [nx, ny, nz] = size(array);
    fid = fopen(filename, 'wt');
    if fid == -1
        error('write_vtk_Volume:fopen', 'Could not open %s for writing.', filename);
    end
    fprintf(fid, '# vtk DataFile Version 2.0\n');
    fprintf(fid, 'Comment goes here\n');
    fprintf(fid, 'ASCII\n');
    fprintf(fid, '\n');
    fprintf(fid, 'DATASET STRUCTURED_POINTS\n');
    fprintf(fid, 'DIMENSIONS    %d   %d   %d\n', nx, ny, nz);
    fprintf(fid, '\n');
    fprintf(fid, 'ORIGIN    0.000   0.000   0.000\n');
    fprintf(fid, 'SPACING   %g   %g   %g\n', Spacing(1), Spacing(2), Spacing(3));
    fprintf(fid, '\n');
    fprintf(fid, 'POINT_DATA   %d\n', nx*ny*nz);
    fprintf(fid, 'SCALARS scalars double\n');
    fprintf(fid, 'LOOKUP_TABLE default\n');
    fprintf(fid, '\n');

    % VTK STRUCTURED_POINTS order is x fastest, then y, then z, which matches
    % MATLAB's column-major linear order of an (nx,ny,nz) array. Write the whole
    % volume in one vectorized call (nx values per line) so the export cannot be
    % truncated by a slow per-voxel loop.
    values = reshape(double(array), nx, []);
    fprintf(fid, [repmat('%g ', 1, nx) '\n'], values);

    fclose(fid);
return
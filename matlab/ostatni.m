clc
clear

axes = readmatrix("main_for_matlab.csv");
data = readmatrix("nonstandarised.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "wielomiany", figOpt{:});
plot(axes(1,:), axes(3,:), 'r*')
hold on
plot(axes(1,:), data(3,:), 'Color', '#77AC30', 'LineStyle', '-')
plot(axes(1,:), data(4,:), 'b-')
grid;
xlabel("czas [dni]");
ylabel("temperatura [°C]");
clc
clear

data = readmatrix("main_for_matlab.csv");

figOpt = {'Position', [300, 300, 800, 500], 'DefaultAxesFontSize', 13};

f1 = figure('Name', "U na X", figOpt{:});
plot(data(1,:), data(3,:), 'r*')
grid;
xlabel("czas [s]");
ylabel("temperatura [°C]");

f2 = figure('Name', 'U na T', figOpt{:});
plot(data(2,:), data(3,:), 'r*');
grid;
xlabel("zmienna standaryzowana");
ylabel("temperatura [°C]");

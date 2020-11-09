%% Breguet Weite fuer ein Propellerflugzeug (Erdumrundung)

Wratio = 11;    % Erdumrundung
SFC_SI = 15e-6;   % Specific fuel consumption

V = 196*0.277778;    % Fluggeschwindigkeit
g = 9.81;    % Gravitationskonstante
L_D = 27;    % L/D; Lift-2-Drag ratio
%C = V/g*L_D/SFC_SI*0.000621371*1.60934;
C = 1e4;
R = C*log(Wratio)    % Weite in km

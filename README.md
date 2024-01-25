# nl2mtl
Automatic Extraction and Formalization of Temporal Requirements from Text: A Survey


| Paper title                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                        | Output (Formal Language)                                     | Example                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **(1)** A Comprehensive Requirement Capturing Model Enabling the Automated Formalisation of NL Requirements <br/> **(2)** RCM-Extractor: An Automated NLP-Based Approach for Extracting a Semi Formal Representation Model from Natural Language Requirements<br/> **(3)** ARF: Automatic Requirements Formalisation Tool | If a valid blood_pressure is unavailable after at least 180 sec, manual_mode should be triggered.                                                                                                                                                                                                                                              | Metric Temporal Logic (Optional: Computation Tree Logic)     | G( [F{t>=180}(a valid blood_pressure = unavailable)] ==> [manual_mode.crrStatus = triggered] )                        |
| AUTOMATE - Mapping natural language procedures descriptions to linear temporal logic templates: an application in the surgical robotic domain                                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                              | Linear Temporal Logic Template                               | -                                                                                                                     |
| Automatic Generation of Specification from Natural Language Based on Temporal Logic                                                                                                                                                                                                                                       | -                                                                                                                                                                                                                                                                                                                                              | -                                                            | -                                                                                                                     |
| Data-Efficient Learning of Natural Language to Linear Temporal Logic Translators for Robot Task Specification                                                                                                                                                                                                             | Instead of going through the red room move through the blue room to enter the green room.                                                                                                                                                                                                                                                      | Linear Temporal Logic                                        | F & B F C                                                                                                             |
| DeepSTL - From English Requirements to Signal Temporal Logic                                                                                                                                                                                                                                                              | At a certain time instant in less than 1695 time units, eventually the transition action that V i W r E c changes to G O R Y e m x 6 8 will have to get detected.                                                                                                                                                                              | Signal Temporal Logic                                        | eventually [0:1695] (rise (V i W r E c == G O R Y e m x 6 8))                                                         |
| Formal Specifications from Natural Language                                                                                                                                                                                                                                                                               | -                                                                                                                                                                                                                                                                                                                                              | Regular Expression, First-order Logic, Linear Temporal Logic | -                                                                                                                     |
| Formalization of Natural Language into PPTL Specification via Neural Machine Translation                                                                                                                                                                                                                                  | If cuff and arterial_line and pulse_wave are not available in 60 seconds, next manual_mode is started.                                                                                                                                                                                                                                         | Propositional Projection Temporal Logic                      | G ( !(cuff & arterial_line & pulse_wave) U[0,60] manual_mode )                                                        |
| Lang2LTL - Generating Natural Language From Logic Expressions With Structural Representation                                                                                                                                                                                                                              | Keep going to a and b in arbitrary order.                                                                                                                                                                                                                                                                                                      | Linear Temporal Logic                                        | & G F a G F b                                                                                                         |
| Leveraging Natural Language Processing for a Consistency Checking Toolchain of Automotive Requirements                                                                                                                                                                                                                    | -                                                                                                                                                                                                                                                                                                                                              | Timed Computation Tree Logic Formalization                   | -                                                                                                                     |
| LTLTalk - Interactive Synthesis of Temporal Specifications from Examples and Natural Language                                                                                                                                                                                                                             | Get one triangle from [4,0] and then one item from [11,1].                                                                                                                                                                                                                                                                                     | Linear Temporal Logic                                        | before(pick_one_x_triangle_item_at_4_0,pick_one_x_x_item_at_11_1)                                                     |
| NL2TL: Transforming Natural Languages to Temporal Logics using  Large Language Models                                                                                                                                                                                                                                     | During the interval that signal_1_n stays larger than 11.4 and below 72.4, and the signal_2_n signal is in signal_3_n, then the following condition holds: after a certain time point within 6 time units, signal_4_n will have to be 71.3 and then should keep like that uninterruptedly for every moment during the following 44 time units. | Signal Temporal Logic                                        | G ( (signal_1_n > 11.4 & signal_1_n < 72.4) & signal_2_n == signal_3_n -> F [0:6] ( G [0:44] (signal_4_n == 71.3) ) ) |
| nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models                                                                                                                                                                                                            | If it is the case that every a is eventually followed by a b, then c needs to holds infinitely often.                                                                                                                                                                                                                                          | Linear Temporal Logic (Optional: Signal Temporal Logic)      | G(a -> F b) -> G F c                                                                                                             |

Technical Report on Neural Language Models and Few-Shot Learning for Systematic Requirements  Processing in MDSE - https://www.se-rwth.de/publications/Technical-Report-on-Neural-Language-Models-and-Few-Shot-Learning-for-Systematic-Requirements-Processing-in-MDSE.pdf

Component and Connector Views in Practice: An Experience Report - https://www.se-rwth.de/publications/Component-and-Connector-Views-in-Practice-An-Experience-Report.pdf

AUTOMATE - Mapping natural language procedures descriptions to linear temporal logic templates: an application in the surgical robotic domain - https://gitlab.com/altairLab/AUTOMATE - only if_procedural

nl2spec: Interactively Translating Unstructured Natural Language to Temporal Logics with Large Language Models

Data-Efficient Learning of Natural Language to Linear Temporal Logic Translators for Robot Task Specification

Lang2LTL - https://drive.google.com/drive/folders/1ept4vnvlUevzqUellFt938vV2VDcgdwb

LTLTalk - Interactive Synthesis of Temporal Specifications from Examples and Natural Language

FORMAL SPECIFICATIONS FROM NATURAL LANGUAGE


RCM-Extractor: An Automated NLP-Based Approach for Extracting a Semi Formal Representation Model from Natural Language Requirements
A Comprehensive Requirement Capturing Model Enabling the Automated Formalisation of NL Requirements 
ARF: Automatic Requirements Formalisation Tool

Automatic Generation of Specification from Natural Language Based on Temporal Logic - Modeling take-over performance in level 3 conditionally automated vehicles

DeepSTL - add link

NL2TL: Transforming Natural Languages to Temporal Logics using  Large Language Models

Formalization of Natural Language into PPTL Specification via Neural Machine Translation - Requirement specification extraction and analysis based on propositional projection temporal logic

Leveraging Natural Language Processing for a Consistency Checking Toolchain of Automotive Requirements - add link to requirements


% no tiene sentido - Extracting Software Requirements from Unstructured Documents - PURE 


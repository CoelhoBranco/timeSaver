/*SELECT CURDATE(), current_timestamp(), (
current_timestamp() > CURDATE()
);



*/



SELECT IF (
SELECT atentimento_contador FROM atividade_diaria
where registration_date > curdate()
AND user_id = 1
,

UPDATE FROM atividade_diaria
SET atentimento_contador = atentimento_contador + 1,

INSERT INTO atividade_diaria
(user_id, atentimento_contador) 
VALUES (
1 , 1
)

),


#SELECT * FROM atividade_diaria;
UPDATE atividade_diaria
SET atendimento_contador = atendimento_contador + 1
WHERE id = 3;


SELECT (atendimento_contador) FROM atividade_diaria

where registration_date > curdate()
AND user_id = 1
;


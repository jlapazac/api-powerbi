CREATE PROCEDURE PowerBI.uSp_GetGroups
AS
BEGIN
	SELECT
		[id], [isOnDedicatedCapacity], [isReadOnly], [name]
	FROM [PowerBI].[Groups]
END
GO

CREATE PROCEDURE PowerBI.uSp_GetDatasets
AS
BEGIN
	SELECT
		[addRowsAPIEnabled], [configuredBy], [id], [isEffectiveIdentityRequired], [isEffectiveIdentityRolesRequired], [isOnPremGatewayRequired], [isRefreshable], [name], [targetStorageMode], [groupId]
	FROM [PowerBI].[Datasets]
END
GO

CREATE PROCEDURE PowerBI.uSp_GetRefreshes
AS
BEGIN
	SELECT
		[endTime], [id], [refreshType], [requestId], [serviceExceptionJson], [startTime], [status], [datasetId]
	FROM [PowerBI].[Refreshes]
	WHERE [startTime] >= CAST(CONVERT(VARCHAR(8),GETDATE(),112) AS DATETIME)
END
GO
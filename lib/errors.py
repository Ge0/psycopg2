"""Error classes for PostgreSQL error codes
"""

# Imported for completeness, but unused in this module.
from psycopg2._psycopg import Error, Warning, InterfaceError    # noqa

from psycopg2._psycopg import (
    DataError, DatabaseError, ProgrammingError, IntegrityError,
    InternalError, NotSupportedError, OperationalError,
    QueryCanceledError, TransactionRollbackError)


_by_sqlstate = {}


# autogenerated data: do not edit below this point.


# Class 02 - No Data (this is also a warning class per the SQL standard)


class NoData(DatabaseError):
    pass

_by_sqlstate['02000'] = NoData


class NoAdditionalDynamicResultSetsReturned(DatabaseError):
    pass

_by_sqlstate['02001'] = NoAdditionalDynamicResultSetsReturned


# Class 03 - SQL Statement Not Yet Complete


class SqlStatementNotYetComplete(DatabaseError):
    pass

_by_sqlstate['03000'] = SqlStatementNotYetComplete


# Class 08 - Connection Exception


class ConnectionException(DatabaseError):
    pass

_by_sqlstate['08000'] = ConnectionException


class SqlclientUnableToEstablishSqlconnection(DatabaseError):
    pass

_by_sqlstate['08001'] = SqlclientUnableToEstablishSqlconnection


class ConnectionDoesNotExist(DatabaseError):
    pass

_by_sqlstate['08003'] = ConnectionDoesNotExist


class SqlserverRejectedEstablishmentOfSqlconnection(DatabaseError):
    pass

_by_sqlstate['08004'] = SqlserverRejectedEstablishmentOfSqlconnection


class ConnectionFailure(DatabaseError):
    pass

_by_sqlstate['08006'] = ConnectionFailure


class TransactionResolutionUnknown(DatabaseError):
    pass

_by_sqlstate['08007'] = TransactionResolutionUnknown


class ProtocolViolation(DatabaseError):
    pass

_by_sqlstate['08P01'] = ProtocolViolation


# Class 09 - Triggered Action Exception


class TriggeredActionException(DatabaseError):
    pass

_by_sqlstate['09000'] = TriggeredActionException


# Class 0A - Feature Not Supported


class FeatureNotSupported(NotSupportedError):
    pass

_by_sqlstate['0A000'] = FeatureNotSupported


# Class 0B - Invalid Transaction Initiation


class InvalidTransactionInitiation(DatabaseError):
    pass

_by_sqlstate['0B000'] = InvalidTransactionInitiation


# Class 0F - Locator Exception


class LocatorException(DatabaseError):
    pass

_by_sqlstate['0F000'] = LocatorException


class InvalidLocatorSpecification(DatabaseError):
    pass

_by_sqlstate['0F001'] = InvalidLocatorSpecification


# Class 0L - Invalid Grantor


class InvalidGrantor(DatabaseError):
    pass

_by_sqlstate['0L000'] = InvalidGrantor


class InvalidGrantOperation(DatabaseError):
    pass

_by_sqlstate['0LP01'] = InvalidGrantOperation


# Class 0P - Invalid Role Specification


class InvalidRoleSpecification(DatabaseError):
    pass

_by_sqlstate['0P000'] = InvalidRoleSpecification


# Class 0Z - Diagnostics Exception


class DiagnosticsException(DatabaseError):
    pass

_by_sqlstate['0Z000'] = DiagnosticsException


class StackedDiagnosticsAccessedWithoutActiveHandler(DatabaseError):
    pass

_by_sqlstate['0Z002'] = StackedDiagnosticsAccessedWithoutActiveHandler


# Class 20 - Case Not Found


class CaseNotFound(ProgrammingError):
    pass

_by_sqlstate['20000'] = CaseNotFound


# Class 21 - Cardinality Violation


class CardinalityViolation(ProgrammingError):
    pass

_by_sqlstate['21000'] = CardinalityViolation


# Class 22 - Data Exception


class DataException(DataError):
    pass

_by_sqlstate['22000'] = DataException


class StringDataRightTruncation(DataError):
    pass

_by_sqlstate['22001'] = StringDataRightTruncation


class NullValueNoIndicatorParameter(DataError):
    pass

_by_sqlstate['22002'] = NullValueNoIndicatorParameter


class NumericValueOutOfRange(DataError):
    pass

_by_sqlstate['22003'] = NumericValueOutOfRange


class NullValueNotAllowed(DataError):
    pass

_by_sqlstate['22004'] = NullValueNotAllowed


class ErrorInAssignment(DataError):
    pass

_by_sqlstate['22005'] = ErrorInAssignment


class InvalidDatetimeFormat(DataError):
    pass

_by_sqlstate['22007'] = InvalidDatetimeFormat


class DatetimeFieldOverflow(DataError):
    pass

_by_sqlstate['22008'] = DatetimeFieldOverflow


class InvalidTimeZoneDisplacementValue(DataError):
    pass

_by_sqlstate['22009'] = InvalidTimeZoneDisplacementValue


class EscapeCharacterConflict(DataError):
    pass

_by_sqlstate['2200B'] = EscapeCharacterConflict


class InvalidUseOfEscapeCharacter(DataError):
    pass

_by_sqlstate['2200C'] = InvalidUseOfEscapeCharacter


class InvalidEscapeOctet(DataError):
    pass

_by_sqlstate['2200D'] = InvalidEscapeOctet


class ZeroLengthCharacterString(DataError):
    pass

_by_sqlstate['2200F'] = ZeroLengthCharacterString


class MostSpecificTypeMismatch(DataError):
    pass

_by_sqlstate['2200G'] = MostSpecificTypeMismatch


class SequenceGeneratorLimitExceeded(DataError):
    pass

_by_sqlstate['2200H'] = SequenceGeneratorLimitExceeded


class NotAnXmlDocument(DataError):
    pass

_by_sqlstate['2200L'] = NotAnXmlDocument


class InvalidXmlDocument(DataError):
    pass

_by_sqlstate['2200M'] = InvalidXmlDocument


class InvalidXmlContent(DataError):
    pass

_by_sqlstate['2200N'] = InvalidXmlContent


class InvalidXmlComment(DataError):
    pass

_by_sqlstate['2200S'] = InvalidXmlComment


class InvalidXmlProcessingInstruction(DataError):
    pass

_by_sqlstate['2200T'] = InvalidXmlProcessingInstruction


class InvalidIndicatorParameterValue(DataError):
    pass

_by_sqlstate['22010'] = InvalidIndicatorParameterValue


class SubstringError(DataError):
    pass

_by_sqlstate['22011'] = SubstringError


class DivisionByZero(DataError):
    pass

_by_sqlstate['22012'] = DivisionByZero


class InvalidArgumentForNtileFunction(DataError):
    pass

_by_sqlstate['22014'] = InvalidArgumentForNtileFunction


class IntervalFieldOverflow(DataError):
    pass

_by_sqlstate['22015'] = IntervalFieldOverflow


class InvalidArgumentForNthValueFunction(DataError):
    pass

_by_sqlstate['22016'] = InvalidArgumentForNthValueFunction


class InvalidCharacterValueForCast(DataError):
    pass

_by_sqlstate['22018'] = InvalidCharacterValueForCast


class InvalidEscapeCharacter(DataError):
    pass

_by_sqlstate['22019'] = InvalidEscapeCharacter


class InvalidRegularExpression(DataError):
    pass

_by_sqlstate['2201B'] = InvalidRegularExpression


class InvalidArgumentForLogarithm(DataError):
    pass

_by_sqlstate['2201E'] = InvalidArgumentForLogarithm


class InvalidArgumentForPowerFunction(DataError):
    pass

_by_sqlstate['2201F'] = InvalidArgumentForPowerFunction


class InvalidArgumentForWidthBucketFunction(DataError):
    pass

_by_sqlstate['2201G'] = InvalidArgumentForWidthBucketFunction


class InvalidRowCountInLimitClause(DataError):
    pass

_by_sqlstate['2201W'] = InvalidRowCountInLimitClause


class InvalidRowCountInResultOffsetClause(DataError):
    pass

_by_sqlstate['2201X'] = InvalidRowCountInResultOffsetClause


class CharacterNotInRepertoire(DataError):
    pass

_by_sqlstate['22021'] = CharacterNotInRepertoire


class IndicatorOverflow(DataError):
    pass

_by_sqlstate['22022'] = IndicatorOverflow


class InvalidParameterValue(DataError):
    pass

_by_sqlstate['22023'] = InvalidParameterValue


class UnterminatedCString(DataError):
    pass

_by_sqlstate['22024'] = UnterminatedCString


class InvalidEscapeSequence(DataError):
    pass

_by_sqlstate['22025'] = InvalidEscapeSequence


class StringDataLengthMismatch(DataError):
    pass

_by_sqlstate['22026'] = StringDataLengthMismatch


class TrimError(DataError):
    pass

_by_sqlstate['22027'] = TrimError


class ArraySubscriptError(DataError):
    pass

_by_sqlstate['2202E'] = ArraySubscriptError


class InvalidTablesampleRepeat(DataError):
    pass

_by_sqlstate['2202G'] = InvalidTablesampleRepeat


class InvalidTablesampleArgument(DataError):
    pass

_by_sqlstate['2202H'] = InvalidTablesampleArgument


class FloatingPointException(DataError):
    pass

_by_sqlstate['22P01'] = FloatingPointException


class InvalidTextRepresentation(DataError):
    pass

_by_sqlstate['22P02'] = InvalidTextRepresentation


class InvalidBinaryRepresentation(DataError):
    pass

_by_sqlstate['22P03'] = InvalidBinaryRepresentation


class BadCopyFileFormat(DataError):
    pass

_by_sqlstate['22P04'] = BadCopyFileFormat


class UntranslatableCharacter(DataError):
    pass

_by_sqlstate['22P05'] = UntranslatableCharacter


class NonstandardUseOfEscapeCharacter(DataError):
    pass

_by_sqlstate['22P06'] = NonstandardUseOfEscapeCharacter


# Class 23 - Integrity Constraint Violation


class IntegrityConstraintViolation(IntegrityError):
    pass

_by_sqlstate['23000'] = IntegrityConstraintViolation


class RestrictViolation(IntegrityError):
    pass

_by_sqlstate['23001'] = RestrictViolation


class NotNullViolation(IntegrityError):
    pass

_by_sqlstate['23502'] = NotNullViolation


class ForeignKeyViolation(IntegrityError):
    pass

_by_sqlstate['23503'] = ForeignKeyViolation


class UniqueViolation(IntegrityError):
    pass

_by_sqlstate['23505'] = UniqueViolation


class CheckViolation(IntegrityError):
    pass

_by_sqlstate['23514'] = CheckViolation


class ExclusionViolation(IntegrityError):
    pass

_by_sqlstate['23P01'] = ExclusionViolation


# Class 24 - Invalid Cursor State


class InvalidCursorState(InternalError):
    pass

_by_sqlstate['24000'] = InvalidCursorState


# Class 25 - Invalid Transaction State


class InvalidTransactionState(InternalError):
    pass

_by_sqlstate['25000'] = InvalidTransactionState


class ActiveSqlTransaction(InternalError):
    pass

_by_sqlstate['25001'] = ActiveSqlTransaction


class BranchTransactionAlreadyActive(InternalError):
    pass

_by_sqlstate['25002'] = BranchTransactionAlreadyActive


class InappropriateAccessModeForBranchTransaction(InternalError):
    pass

_by_sqlstate['25003'] = InappropriateAccessModeForBranchTransaction


class InappropriateIsolationLevelForBranchTransaction(InternalError):
    pass

_by_sqlstate['25004'] = InappropriateIsolationLevelForBranchTransaction


class NoActiveSqlTransactionForBranchTransaction(InternalError):
    pass

_by_sqlstate['25005'] = NoActiveSqlTransactionForBranchTransaction


class ReadOnlySqlTransaction(InternalError):
    pass

_by_sqlstate['25006'] = ReadOnlySqlTransaction


class SchemaAndDataStatementMixingNotSupported(InternalError):
    pass

_by_sqlstate['25007'] = SchemaAndDataStatementMixingNotSupported


class HeldCursorRequiresSameIsolationLevel(InternalError):
    pass

_by_sqlstate['25008'] = HeldCursorRequiresSameIsolationLevel


class NoActiveSqlTransaction(InternalError):
    pass

_by_sqlstate['25P01'] = NoActiveSqlTransaction


class InFailedSqlTransaction(InternalError):
    pass

_by_sqlstate['25P02'] = InFailedSqlTransaction


class IdleInTransactionSessionTimeout(InternalError):
    pass

_by_sqlstate['25P03'] = IdleInTransactionSessionTimeout


# Class 26 - Invalid SQL Statement Name


class InvalidSqlStatementName(OperationalError):
    pass

_by_sqlstate['26000'] = InvalidSqlStatementName


# Class 27 - Triggered Data Change Violation


class TriggeredDataChangeViolation(OperationalError):
    pass

_by_sqlstate['27000'] = TriggeredDataChangeViolation


# Class 28 - Invalid Authorization Specification


class InvalidAuthorizationSpecification(OperationalError):
    pass

_by_sqlstate['28000'] = InvalidAuthorizationSpecification


class InvalidPassword(OperationalError):
    pass

_by_sqlstate['28P01'] = InvalidPassword


# Class 2B - Dependent Privilege Descriptors Still Exist


class DependentPrivilegeDescriptorsStillExist(InternalError):
    pass

_by_sqlstate['2B000'] = DependentPrivilegeDescriptorsStillExist


class DependentObjectsStillExist(InternalError):
    pass

_by_sqlstate['2BP01'] = DependentObjectsStillExist


# Class 2D - Invalid Transaction Termination


class InvalidTransactionTermination(InternalError):
    pass

_by_sqlstate['2D000'] = InvalidTransactionTermination


# Class 2F - SQL Routine Exception


class SqlRoutineException(InternalError):
    pass

_by_sqlstate['2F000'] = SqlRoutineException


class ModifyingSqlDataNotPermitted(InternalError):
    pass

_by_sqlstate['2F002'] = ModifyingSqlDataNotPermitted


class ProhibitedSqlStatementAttempted(InternalError):
    pass

_by_sqlstate['2F003'] = ProhibitedSqlStatementAttempted


class ReadingSqlDataNotPermitted(InternalError):
    pass

_by_sqlstate['2F004'] = ReadingSqlDataNotPermitted


class FunctionExecutedNoReturnStatement(InternalError):
    pass

_by_sqlstate['2F005'] = FunctionExecutedNoReturnStatement


# Class 34 - Invalid Cursor Name


class InvalidCursorName(OperationalError):
    pass

_by_sqlstate['34000'] = InvalidCursorName


# Class 38 - External Routine Exception


class ExternalRoutineException(InternalError):
    pass

_by_sqlstate['38000'] = ExternalRoutineException


class ContainingSqlNotPermitted(InternalError):
    pass

_by_sqlstate['38001'] = ContainingSqlNotPermitted


class ModifyingSqlDataNotPermitted(InternalError):
    pass

_by_sqlstate['38002'] = ModifyingSqlDataNotPermitted


class ProhibitedSqlStatementAttempted(InternalError):
    pass

_by_sqlstate['38003'] = ProhibitedSqlStatementAttempted


class ReadingSqlDataNotPermitted(InternalError):
    pass

_by_sqlstate['38004'] = ReadingSqlDataNotPermitted


# Class 39 - External Routine Invocation Exception


class ExternalRoutineInvocationException(InternalError):
    pass

_by_sqlstate['39000'] = ExternalRoutineInvocationException


class InvalidSqlstateReturned(InternalError):
    pass

_by_sqlstate['39001'] = InvalidSqlstateReturned


class NullValueNotAllowed(InternalError):
    pass

_by_sqlstate['39004'] = NullValueNotAllowed


class TriggerProtocolViolated(InternalError):
    pass

_by_sqlstate['39P01'] = TriggerProtocolViolated


class SrfProtocolViolated(InternalError):
    pass

_by_sqlstate['39P02'] = SrfProtocolViolated


class EventTriggerProtocolViolated(InternalError):
    pass

_by_sqlstate['39P03'] = EventTriggerProtocolViolated


# Class 3B - Savepoint Exception


class SavepointException(InternalError):
    pass

_by_sqlstate['3B000'] = SavepointException


class InvalidSavepointSpecification(InternalError):
    pass

_by_sqlstate['3B001'] = InvalidSavepointSpecification


# Class 3D - Invalid Catalog Name


class InvalidCatalogName(DatabaseError):
    pass

_by_sqlstate['3D000'] = InvalidCatalogName


# Class 3F - Invalid Schema Name


class InvalidSchemaName(DatabaseError):
    pass

_by_sqlstate['3F000'] = InvalidSchemaName


# Class 40 - Transaction Rollback


class TransactionRollback(TransactionRollbackError):
    pass

_by_sqlstate['40000'] = TransactionRollback


class SerializationFailure(TransactionRollbackError):
    pass

_by_sqlstate['40001'] = SerializationFailure


class TransactionIntegrityConstraintViolation(TransactionRollbackError):
    pass

_by_sqlstate['40002'] = TransactionIntegrityConstraintViolation


class StatementCompletionUnknown(TransactionRollbackError):
    pass

_by_sqlstate['40003'] = StatementCompletionUnknown


class DeadlockDetected(TransactionRollbackError):
    pass

_by_sqlstate['40P01'] = DeadlockDetected


# Class 42 - Syntax Error or Access Rule Violation


class SyntaxErrorOrAccessRuleViolation(ProgrammingError):
    pass

_by_sqlstate['42000'] = SyntaxErrorOrAccessRuleViolation


class InsufficientPrivilege(ProgrammingError):
    pass

_by_sqlstate['42501'] = InsufficientPrivilege


class SyntaxError(ProgrammingError):
    pass

_by_sqlstate['42601'] = SyntaxError


class InvalidName(ProgrammingError):
    pass

_by_sqlstate['42602'] = InvalidName


class InvalidColumnDefinition(ProgrammingError):
    pass

_by_sqlstate['42611'] = InvalidColumnDefinition


class NameTooLong(ProgrammingError):
    pass

_by_sqlstate['42622'] = NameTooLong


class DuplicateColumn(ProgrammingError):
    pass

_by_sqlstate['42701'] = DuplicateColumn


class AmbiguousColumn(ProgrammingError):
    pass

_by_sqlstate['42702'] = AmbiguousColumn


class UndefinedColumn(ProgrammingError):
    pass

_by_sqlstate['42703'] = UndefinedColumn


class UndefinedObject(ProgrammingError):
    pass

_by_sqlstate['42704'] = UndefinedObject


class DuplicateObject(ProgrammingError):
    pass

_by_sqlstate['42710'] = DuplicateObject


class DuplicateAlias(ProgrammingError):
    pass

_by_sqlstate['42712'] = DuplicateAlias


class DuplicateFunction(ProgrammingError):
    pass

_by_sqlstate['42723'] = DuplicateFunction


class AmbiguousFunction(ProgrammingError):
    pass

_by_sqlstate['42725'] = AmbiguousFunction


class GroupingError(ProgrammingError):
    pass

_by_sqlstate['42803'] = GroupingError


class DatatypeMismatch(ProgrammingError):
    pass

_by_sqlstate['42804'] = DatatypeMismatch


class WrongObjectType(ProgrammingError):
    pass

_by_sqlstate['42809'] = WrongObjectType


class InvalidForeignKey(ProgrammingError):
    pass

_by_sqlstate['42830'] = InvalidForeignKey


class CannotCoerce(ProgrammingError):
    pass

_by_sqlstate['42846'] = CannotCoerce


class UndefinedFunction(ProgrammingError):
    pass

_by_sqlstate['42883'] = UndefinedFunction


class GeneratedAlways(ProgrammingError):
    pass

_by_sqlstate['428C9'] = GeneratedAlways


class ReservedName(ProgrammingError):
    pass

_by_sqlstate['42939'] = ReservedName


class UndefinedTable(ProgrammingError):
    pass

_by_sqlstate['42P01'] = UndefinedTable


class UndefinedParameter(ProgrammingError):
    pass

_by_sqlstate['42P02'] = UndefinedParameter


class DuplicateCursor(ProgrammingError):
    pass

_by_sqlstate['42P03'] = DuplicateCursor


class DuplicateDatabase(ProgrammingError):
    pass

_by_sqlstate['42P04'] = DuplicateDatabase


class DuplicatePreparedStatement(ProgrammingError):
    pass

_by_sqlstate['42P05'] = DuplicatePreparedStatement


class DuplicateSchema(ProgrammingError):
    pass

_by_sqlstate['42P06'] = DuplicateSchema


class DuplicateTable(ProgrammingError):
    pass

_by_sqlstate['42P07'] = DuplicateTable


class AmbiguousParameter(ProgrammingError):
    pass

_by_sqlstate['42P08'] = AmbiguousParameter


class AmbiguousAlias(ProgrammingError):
    pass

_by_sqlstate['42P09'] = AmbiguousAlias


class InvalidColumnReference(ProgrammingError):
    pass

_by_sqlstate['42P10'] = InvalidColumnReference


class InvalidCursorDefinition(ProgrammingError):
    pass

_by_sqlstate['42P11'] = InvalidCursorDefinition


class InvalidDatabaseDefinition(ProgrammingError):
    pass

_by_sqlstate['42P12'] = InvalidDatabaseDefinition


class InvalidFunctionDefinition(ProgrammingError):
    pass

_by_sqlstate['42P13'] = InvalidFunctionDefinition


class InvalidPreparedStatementDefinition(ProgrammingError):
    pass

_by_sqlstate['42P14'] = InvalidPreparedStatementDefinition


class InvalidSchemaDefinition(ProgrammingError):
    pass

_by_sqlstate['42P15'] = InvalidSchemaDefinition


class InvalidTableDefinition(ProgrammingError):
    pass

_by_sqlstate['42P16'] = InvalidTableDefinition


class InvalidObjectDefinition(ProgrammingError):
    pass

_by_sqlstate['42P17'] = InvalidObjectDefinition


class IndeterminateDatatype(ProgrammingError):
    pass

_by_sqlstate['42P18'] = IndeterminateDatatype


class InvalidRecursion(ProgrammingError):
    pass

_by_sqlstate['42P19'] = InvalidRecursion


class WindowingError(ProgrammingError):
    pass

_by_sqlstate['42P20'] = WindowingError


class CollationMismatch(ProgrammingError):
    pass

_by_sqlstate['42P21'] = CollationMismatch


class IndeterminateCollation(ProgrammingError):
    pass

_by_sqlstate['42P22'] = IndeterminateCollation


# Class 44 - WITH CHECK OPTION Violation


class WithCheckOptionViolation(ProgrammingError):
    pass

_by_sqlstate['44000'] = WithCheckOptionViolation


# Class 53 - Insufficient Resources


class InsufficientResources(OperationalError):
    pass

_by_sqlstate['53000'] = InsufficientResources


class DiskFull(OperationalError):
    pass

_by_sqlstate['53100'] = DiskFull


class OutOfMemory(OperationalError):
    pass

_by_sqlstate['53200'] = OutOfMemory


class TooManyConnections(OperationalError):
    pass

_by_sqlstate['53300'] = TooManyConnections


class ConfigurationLimitExceeded(OperationalError):
    pass

_by_sqlstate['53400'] = ConfigurationLimitExceeded


# Class 54 - Program Limit Exceeded


class ProgramLimitExceeded(OperationalError):
    pass

_by_sqlstate['54000'] = ProgramLimitExceeded


class StatementTooComplex(OperationalError):
    pass

_by_sqlstate['54001'] = StatementTooComplex


class TooManyColumns(OperationalError):
    pass

_by_sqlstate['54011'] = TooManyColumns


class TooManyArguments(OperationalError):
    pass

_by_sqlstate['54023'] = TooManyArguments


# Class 55 - Object Not In Prerequisite State


class ObjectNotInPrerequisiteState(OperationalError):
    pass

_by_sqlstate['55000'] = ObjectNotInPrerequisiteState


class ObjectInUse(OperationalError):
    pass

_by_sqlstate['55006'] = ObjectInUse


class CantChangeRuntimeParam(OperationalError):
    pass

_by_sqlstate['55P02'] = CantChangeRuntimeParam


class LockNotAvailable(OperationalError):
    pass

_by_sqlstate['55P03'] = LockNotAvailable


# Class 57 - Operator Intervention


class OperatorIntervention(OperationalError):
    pass

_by_sqlstate['57000'] = OperatorIntervention


class QueryCanceled(QueryCanceledError):
    pass

_by_sqlstate['57014'] = QueryCanceled


class AdminShutdown(OperationalError):
    pass

_by_sqlstate['57P01'] = AdminShutdown


class CrashShutdown(OperationalError):
    pass

_by_sqlstate['57P02'] = CrashShutdown


class CannotConnectNow(OperationalError):
    pass

_by_sqlstate['57P03'] = CannotConnectNow


class DatabaseDropped(OperationalError):
    pass

_by_sqlstate['57P04'] = DatabaseDropped


# Class 58 - System Error (errors external to PostgreSQL itself)


class SystemError(OperationalError):
    pass

_by_sqlstate['58000'] = SystemError


class IoError(OperationalError):
    pass

_by_sqlstate['58030'] = IoError


class UndefinedFile(OperationalError):
    pass

_by_sqlstate['58P01'] = UndefinedFile


class DuplicateFile(OperationalError):
    pass

_by_sqlstate['58P02'] = DuplicateFile


# Class 72 - Snapshot Failure


class SnapshotTooOld(DatabaseError):
    pass

_by_sqlstate['72000'] = SnapshotTooOld


# Class F0 - Configuration File Error


class ConfigFileError(InternalError):
    pass

_by_sqlstate['F0000'] = ConfigFileError


class LockFileExists(InternalError):
    pass

_by_sqlstate['F0001'] = LockFileExists


# Class HV - Foreign Data Wrapper Error (SQL/MED)


class FdwError(OperationalError):
    pass

_by_sqlstate['HV000'] = FdwError


class FdwOutOfMemory(OperationalError):
    pass

_by_sqlstate['HV001'] = FdwOutOfMemory


class FdwDynamicParameterValueNeeded(OperationalError):
    pass

_by_sqlstate['HV002'] = FdwDynamicParameterValueNeeded


class FdwInvalidDataType(OperationalError):
    pass

_by_sqlstate['HV004'] = FdwInvalidDataType


class FdwColumnNameNotFound(OperationalError):
    pass

_by_sqlstate['HV005'] = FdwColumnNameNotFound


class FdwInvalidDataTypeDescriptors(OperationalError):
    pass

_by_sqlstate['HV006'] = FdwInvalidDataTypeDescriptors


class FdwInvalidColumnName(OperationalError):
    pass

_by_sqlstate['HV007'] = FdwInvalidColumnName


class FdwInvalidColumnNumber(OperationalError):
    pass

_by_sqlstate['HV008'] = FdwInvalidColumnNumber


class FdwInvalidUseOfNullPointer(OperationalError):
    pass

_by_sqlstate['HV009'] = FdwInvalidUseOfNullPointer


class FdwInvalidStringFormat(OperationalError):
    pass

_by_sqlstate['HV00A'] = FdwInvalidStringFormat


class FdwInvalidHandle(OperationalError):
    pass

_by_sqlstate['HV00B'] = FdwInvalidHandle


class FdwInvalidOptionIndex(OperationalError):
    pass

_by_sqlstate['HV00C'] = FdwInvalidOptionIndex


class FdwInvalidOptionName(OperationalError):
    pass

_by_sqlstate['HV00D'] = FdwInvalidOptionName


class FdwOptionNameNotFound(OperationalError):
    pass

_by_sqlstate['HV00J'] = FdwOptionNameNotFound


class FdwReplyHandle(OperationalError):
    pass

_by_sqlstate['HV00K'] = FdwReplyHandle


class FdwUnableToCreateExecution(OperationalError):
    pass

_by_sqlstate['HV00L'] = FdwUnableToCreateExecution


class FdwUnableToCreateReply(OperationalError):
    pass

_by_sqlstate['HV00M'] = FdwUnableToCreateReply


class FdwUnableToEstablishConnection(OperationalError):
    pass

_by_sqlstate['HV00N'] = FdwUnableToEstablishConnection


class FdwNoSchemas(OperationalError):
    pass

_by_sqlstate['HV00P'] = FdwNoSchemas


class FdwSchemaNotFound(OperationalError):
    pass

_by_sqlstate['HV00Q'] = FdwSchemaNotFound


class FdwTableNotFound(OperationalError):
    pass

_by_sqlstate['HV00R'] = FdwTableNotFound


class FdwFunctionSequenceError(OperationalError):
    pass

_by_sqlstate['HV010'] = FdwFunctionSequenceError


class FdwTooManyHandles(OperationalError):
    pass

_by_sqlstate['HV014'] = FdwTooManyHandles


class FdwInconsistentDescriptorInformation(OperationalError):
    pass

_by_sqlstate['HV021'] = FdwInconsistentDescriptorInformation


class FdwInvalidAttributeValue(OperationalError):
    pass

_by_sqlstate['HV024'] = FdwInvalidAttributeValue


class FdwInvalidStringLengthOrBufferLength(OperationalError):
    pass

_by_sqlstate['HV090'] = FdwInvalidStringLengthOrBufferLength


class FdwInvalidDescriptorFieldIdentifier(OperationalError):
    pass

_by_sqlstate['HV091'] = FdwInvalidDescriptorFieldIdentifier


# Class P0 - PL/pgSQL Error


class PlpgsqlError(InternalError):
    pass

_by_sqlstate['P0000'] = PlpgsqlError


class RaiseException(InternalError):
    pass

_by_sqlstate['P0001'] = RaiseException


class NoDataFound(InternalError):
    pass

_by_sqlstate['P0002'] = NoDataFound


class TooManyRows(InternalError):
    pass

_by_sqlstate['P0003'] = TooManyRows


class AssertFailure(InternalError):
    pass

_by_sqlstate['P0004'] = AssertFailure


# Class XX - Internal Error


class InternalError(InternalError):
    pass

_by_sqlstate['XX000'] = InternalError


class DataCorrupted(InternalError):
    pass

_by_sqlstate['XX001'] = DataCorrupted


class IndexCorrupted(InternalError):
    pass

_by_sqlstate['XX002'] = IndexCorrupted
